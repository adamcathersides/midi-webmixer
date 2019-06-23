from flask import Flask, request
from flask_restful import Api, Resource
import send_cc

app = Flask(__name__)
api = Api(app)

# aux_map[aux][channel]
aux_map = {
        'aux1':{1:1,  2:2,  3:3,  4:4,  5:5,  6:6,  7:7,  8:8,  9:9,  10:10, 11:11, 12:12},
        'aux2':{1:13, 2:14, 3:15, 4:16, 5:17, 6:18, 7:19, 8:20, 9:21, 10:22, 11:23, 12:24},
        'aux3':{1:25, 2:26, 3:27, 4:28, 5:29, 6:30, 7:31, 8:32, 9:33, 10:34, 11:35, 12:36},
        'aux4':{1:37, 2:38, 3:39, 4:40, 5:41, 6:42, 7:43, 8:44, 9:45, 10:46, 11:47, 12:48}
        }

class Mixer(Resource):

    def __init__(self):
        self.midi = send_cc.midi(3)

    def post(self, aux, channel, value):

        cc = aux_map[f'aux{aux}'][channel]

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
    app.run(debug=True, host='0.0.0.0', port=5001)
