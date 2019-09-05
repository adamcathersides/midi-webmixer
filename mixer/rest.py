from flask import Flask, request
from flask_restful import Api, Resource
import mixer.send_cc as send_cc
import json
import os
from mixer.config import ConfigCheck

app = Flask(__name__)
api = Api(app)


def _createChannelMap():

    """"
    Auto generate the channel map like so:

    {"aux1": {"channel1": {"cc": 0, "value": 74}....}
    """

    mix_map = {}
    for mix in range(1,5):
        mix_map[f'aux{mix}'] = {}
        for channel in range(0,12):
            # Generate offsets for cc numbers
            if mix == 1:
                offset = 0
            elif mix == 2:
                offset = 12
            elif mix == 3:
                offset = 24
            elif mix == 4:
                offset = 36
            mix_map[f'aux{mix}'][f'channel{channel+1}'] = {'cc':channel + offset, 'value':0}
    return mix_map


class Mixer(Resource):

    def __init__(self):


        self.midi = send_cc.midi(cfg['Midi']['port'])

        if os.path.isfile('/tmp/channelmap.json'):
            with open('/tmp/channelmap.json', 'r') as mapfile:
                self.channelMap = json.load(mapfile)
        else:
            self.channelMap = _createChannelMap()

    def post(self, aux, channel, value):

        cc = self.channelMap[f'aux{aux}'][f'channel{channel}']['cc']
        self.channelMap[f'aux{aux}'][f'channel{channel}']['value'] = value

        with open('channelmap.json', 'w') as mapfile:
            json.dump(self.channelMap, mapfile)

        self.midi.cc_tx(cc, value)
        return {f'aux{aux}':{channel:value}}

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

cfg = ConfigCheck().parse()

api.add_resource(Mixer, '/mixer/aux<int:aux>/<int:channel>/<int:value>', endpoint = 'mixer')

def run(port, debug):
    app.run(debug=debug, host='0.0.0.0', port=port)

if __name__ == '__main__':
    run()
