from flask import (Flask, render_template, request)

from salary_prediction import SalaryModel

app = Flask(__name__)
model = SalaryModel()


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/survey', methods=('GET', 'POST'))
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        age = request.form['age']
        country = request.form['country']
        industry = request.form['industry']
        role = request.form['role']
        experience = request.form['experience']
        activities = request.form.to_dict(flat=False)['activities']

        sample = model.form_input_to_sample(age, country, industry, role, experience, activities)

        buckets = ['0-10,000', '10-20,000', '20-30,000', '30-40,000', '40-50,000',
         '50-60,000', '60-70,000', '70-80,000', '80-90,000', '90-100,000',
         '100-125,000', '125-150,000', '150-200,000', '200-250,000', '>250,000']

        (salary_index, dist) = model.predict(sample)
        return render_template('prediction.html', salary=buckets[salary_index], salary_distribution=dist)


@app.route('/recommendation', methods=('GET', 'POST'))
def recommendation():
    if request.method == 'GET':
        return render_template('rec_form.html')
    if request.method == 'POST'():
        return render_template('recommendation.html')


if __name__ == '__main__':
    app.run()
