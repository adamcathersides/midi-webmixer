#!/usr/bin/env python3

import click
import mixer.mixer
import mixer.rest
import netifaces
from mixer.config import ConfigCheck
from rtmidi import midiutil

@click.command()
@click.option('--config', required=True, type=str)
@click.option('--gui', is_flag=True)
@click.option('--restapi', is_flag=True)
@click.option('--port', default=5000, type=int)
@click.option('--debug', is_flag=True)
@click.option('--listmidi', is_flag=True, callback=midiutil.list_output_ports())
def start(config, gui, restapi, port, debug, listmidi):

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
    else:
        print('Please select --gui or --restapi')

if __name__ == '__main__':
    start()
