import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('form', __name__, url_prefix='/form')


@bp.route('/form', methods=('GET', 'POST'))
def form():
    return render_template('form.html' if request.method == 'GET' else 'prediction.html')