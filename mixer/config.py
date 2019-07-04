import configparser
import os
import sys

CONFIG_FILE = 'config.ini'

DEFAULT_CONFIG = ({'Network':{'interface':''},
    'Midi': {'port':''},
    'ChannelNames':{
        '1':'',
        '2':'',
        '3':'',
        '4':'',
        '5':'',
        '6':'',
        '7':'',
        '8':'',
        '9':'',
        '10':'',
        '11':'',
        '12':''
        }
        })

class ConfigCheck:

    def __init__(self):

        if not os.path.isfile(f'./{CONFIG_FILE}'):
            print(f'\nCannot find config file therefore writing default file to {CONFIG_FILE}.'
                  '\nPlease review config and rerun')
            self.write_config()
            sys.exit(1)

        self.config = configparser.ConfigParser()

    def parse(self):
        self.read_config()
        return self.config



    def write_config(self, filename=CONFIG_FILE):
        with open(filename, 'w') as configfile:
            self.config.write(configfile)

    def read_config(self, filename=CONFIG_FILE):
        cfg = self.config.read(filename)


