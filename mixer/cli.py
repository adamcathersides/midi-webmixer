#!/usr/bin/env python3

import click
import mixer.mixer
import mixer.rest
import netifaces
from mixer.config import ConfigCheck
from rtmidi import midiutil


def print_midiports(ctx, param, value):

    if not value or ctx.resilient_parsing:
        return
    click.echo(midiutil.list_output_ports())
    ctx.exit()


@click.command()
@click.argument('config', type=click.Path(exists=True))
@click.option('--gui', is_flag=True)
@click.option('--restapi', is_flag=True)
@click.option('--port', default=5000, type=int)
@click.option('--debug', is_flag=True)
@click.option('--listmidi', is_flag=True, is_eager=True, expose_value=False, callback=print_midiports)
def start(config, gui, restapi, port, debug):

    """
    Read config and start the app
    """

    c = ConfigCheck(config)
    cfg = c.parse()
    interface = cfg['Network']['Interface']
    ip_addr = netifaces.ifaddresses(interface)[2][0]['addr']
    channel_names = cfg['ChannelNames']
    midi_port = cfg['Midi']['Port']

    if gui:
        mixer.mixer.run(port, debug, channel_names, ip_addr)
    if restapi:
        mixer.rest.run(port, debug, midi_port)

if __name__ == '__main__':
    start()
