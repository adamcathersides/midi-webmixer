import rtmidi

def tx(control_number, value):

    midiout = rtmidi.MidiOut()

    midiout.open_port(3)

    message = [0xB0, int(control_number), int(value)]
    midiout.send_message(message)
    del midiout
