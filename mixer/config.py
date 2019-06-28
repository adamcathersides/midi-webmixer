import configparser
import os

CONFIG_FILE = 'config.ini'

config = configparser.ConfigParser()
config.read_dict({'Network':{'interface':''},
            'ChannelNames':{}
        })


def write_config(filename=CONFIG_FILE):
    with open(filename, 'w') as configfile:
        config.write(configfile)

def read_config(filename=CONFIG_FILE):
    return config.read(filename)


if os.path.isfile(f'./{CONFIG_FILE}'):
    print('Config exists! Reading..')
    read_config()
else:
    print(f'Cannot find config file. Writing default file to {CONFIG_FILE}')
    write_config()

print(config.sections())
