import configparser
import os
import sys


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

    def __init__(self, config_file):

        self.config_file = config_file
        self.config = configparser.ConfigParser()

        # if not os.path.isfile(f'./{CONFIG_FILE}'):
            # print(f'\nCannot find config file therefore writing default file to {CONFIG_FILE}.'
                  # '\nPlease review config and rerun')
            # self.write_config()
            # sys.exit(1)

    def parse(self):
        self.read_config()
        return self.config

    def write_config(self, filename=config_file):
        self.config.read_dict(DEFAULT_CONFIG)
        with open(filename, 'w') as configfile:
            self.config.write(configfile)

    def read_config(self, filename=self.config_file):
        cfg = self.config.read(filename)


