#!/usr/bin/env python3

import functools
from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
import json
import os

app = Flask(__name__)

@app.route('/mixer/<mix>', methods=('GET', 'POST'))
def mixer(mix):

    with open('/tmp/channelmap.json', 'r') as mapfile:
        channel_map = json.load(mapfile)

    print(app.config['CHANNEL_NAMES'])
    print(app.config['IP_ADDR'])

    return render_template('mixer/mixer.html', ip_addr=app.config['IP_ADDR'], mix=mix, channel_map=channel_map, channel_names=app.config['CHANNEL_NAMES'])


def run(port, debug, channel_names, ip_addr):

    app.config['CHANNEL_NAMES'] = channel_names
    app.config['IP_ADDR'] = ip_addr
    app.run(debug=debug, host='0.0.0.0', port=port)


if __name__ == '__main__':
    run()
