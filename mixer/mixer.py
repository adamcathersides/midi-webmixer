#!/usr/bin/env python3

import functools
from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
import json
import os
import mixer.redis_store as redis_store
import mixer.utils as utils

app = Flask(__name__)

@app.route('/mixer/<mix>', methods=('GET', 'POST'))
def mixer(mix):

    dataStore = redis_store.data()
    print(f'channel_map:{dataStore.get("channel_map")}')
    # if dataStore.get('channel_map'):
        # channel_map = dataStore.get('channel_data')
    # else:
        # channel_map = utils._createChannelMap()

    channel_map = dataStore.get('channel_data')
    print(app.config['CHANNEL_NAMES'])
    print(app.config['IP_ADDR'])

    return render_template('mixer/mixer.html', ip_addr=app.config['IP_ADDR'], mix=mix, channel_map=channel_map, channel_names=app.config['CHANNEL_NAMES'])


def run(port, debug, channel_names, ip_addr):

    app.config['CHANNEL_NAMES'] = channel_names
    app.config['IP_ADDR'] = ip_addr
    app.run(debug=debug, host='0.0.0.0', port=port)


if __name__ == '__main__':
    run()
