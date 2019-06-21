import rtmidi
import time

class midi:

    def __init__(self, midiport):

        self.midiout = rtmidi.MidiOut()
        self.midiout.open_port(midiport)

    def cc_tx(self, control_number, value):

        message = [0xB0, int(control_number), int(value)]
        self.midiout.send_message(message)

    def close(self):
        del self.midiout

