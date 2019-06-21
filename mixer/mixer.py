import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

# from mixer.db import get_db

bp = Blueprint('mixer', __name__, url_prefix='/mixer')

@bp.route('/mixer', methods=('GET', 'POST'))
def mixer():
    if request.method == 'POST':
        channel1 = request.form['channel1']
        channel2 = request.form['channel2']
        channel3 = request.form['channel3']
        channel4 = request.form['channel4']
        # db = get_db()
        error = None

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

        flash(error)

    return render_template('mixer/mixer.html')
