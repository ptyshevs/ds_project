from flask import (
    Blueprint, render_template, request,
)

bp = Blueprint('form', __name__, url_prefix='')


@bp.route('/')
def hello():
    return render_template('hello.html')


@bp.route('/survey', methods=('GET', 'POST'))
def form():
    return render_template('form.html' if request.method == 'GET' else 'prediction.html')