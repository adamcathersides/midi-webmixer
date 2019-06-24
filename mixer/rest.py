from flask import Flask, request
from flask_restful import Api, Resource
import send_cc

app = Flask(__name__)
api = Api(app)

# aux_map[aux][channel]


def _createChannelMmap():
    """ Create the map of mix--> channel--> midi cc number"""

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
        self.midi = send_cc.midi(3)

    def post(self, aux, channel, value):

        cc = channelMap[f'aux{aux}'][f'channel{channel}']['cc']

        self.midi.cc_tx(cc, value)
        return {f'aux{aux}':{channel:value}}

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(Mixer, '/mixer/aux<int:aux>/<int:channel>/<int:value>', endpoint = 'mixer')

if __name__ == '__main__':
    channelMap = _createChannelMmap()
    app.run(debug=True, host='0.0.0.0', port=5001)
