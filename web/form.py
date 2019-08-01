from flask import (Flask, render_template, request)

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/survey', methods=('GET', 'POST'))
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        salary = 60000
        dist = {}
        return render_template('prediction.html', salary=salary, salary_distribution=dist)


@app.route('/recommendation-form')
def recommendation_form():
    return render_template('rec_form.html')


if __name__ == '__main__':
    app.run()
