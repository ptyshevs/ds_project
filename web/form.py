from flask import (
    Blueprint, render_template, request,
)

bp = Blueprint('form', __name__, url_prefix='')


@bp.route('/')
def hello():
    return render_template('hello.html')


@bp.route('/survey', methods=('GET', 'POST'))
def form():
    return render_template('form.html')


@bp.route('/prediction')
def prediction():
    salary = 60000
    dist = {}
    return render_template('prediction.html', salary=salary, salary_distribution=dist)


@bp.route('/recommendation-form')
def recommendation0_form():
    return render_template('rec_form.html')
