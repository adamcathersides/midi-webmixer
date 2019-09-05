import click
import mixer.mixer
import mixer.rest

@click.command()
@click.option('--config', required=True, type=str)
@click.option('--gui', is_flag=True)
@click.option('--restapi', is_flag=True)
@click.option('--port', default=5000, type=int)
@click.option('--debug', is_flag=True)
def start(config, gui, restapi, port, debug):

    if gui:
        mixer.mixer.run(port, debug)
    if restapi:
        mixer.rest.run(port, debug)
    else:
        print('Please select --gui or --restapi')

if __name__ == '__main__':
    start()
