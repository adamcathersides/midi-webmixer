#!/usr/bin/env python3

import functools
import netifaces
from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
import json
from mixer.config import ConfigCheck
import os
# from mixer.db import get_db

app = Flask(__name__)

@app.route('/mixer/<mix>', methods=('GET', 'POST'))
def mixer(mix):

    cfg = ConfigCheck().parse()
    interface = cfg['Network']['Interface']
    ip_addr = netifaces.ifaddresses(interface)[2][0]['addr']

    with open('/tmp/channelmap.json', 'r') as mapfile:
        channel_map = json.load(mapfile)
        # if error is None:
            # db.execute(
                # 'INSERT INTO aux1 (channel1) VALUES (?)',
                # (channel1)
            # )
            # db.execute(
                # 'INSERT INTO aux1 (channel2) VALUES (?)',
                # (channel2)
            # )
            # db.execute(
                # 'INSERT INTO aux1 (channel3) VALUES (?)',
                # (channel3)
            # )
            # db.execute(
                # 'INSERT INTO aux1 (channel4) VALUES (?)',
                # (channel4)
            # )
            # db.commit()
            # return 'done'

    return render_template('mixer/mixer.html', ip_addr=ip_addr, mix=mix, channel_map=channel_map, channel_names=cfg['ChannelNames'])

def run(port, debug):
    app.run(debug=debug, host='0.0.0.0', port=port)

if __name__ == '__main__':
    run()
