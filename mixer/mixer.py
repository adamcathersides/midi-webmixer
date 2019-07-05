#!/usr/bin/env python3

import functools
import netifaces
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
import json
from mixer.config import ConfigCheck
# from mixer.db import get_db

bp = Blueprint('mixer', __name__, url_prefix='/mixer')
cfg = ConfigCheck().parse()

interface = cfg['Network']['Interface']
ip_addr = netifaces.ifaddresses(interface)[2][0]['addr']


@bp.route('/<mix>', methods=('GET', 'POST'))
def mixer(mix):

    with open('mixer/channelmap.json', 'r') as mapfile:
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

