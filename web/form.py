from flask import (
    Blueprint, render_template, request,
)

bp = Blueprint('form', __name__, url_prefix='/form')


@bp.route('', methods=('GET', 'POST'))
def form():
    return render_template('form.html' if request.method == 'GET' else 'prediction.html')