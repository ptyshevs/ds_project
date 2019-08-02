from flask import (Flask, render_template, request)

# from web.salary_prediction import SalaryModel
from salary_prediction import SalaryModel
# from web.recommend import RecommenderModel
from recommend import RecommenderModel

app = Flask(__name__)
model = SalaryModel()
recom_model = RecommenderModel()


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
        activities = request.form.to_dict(flat=False)['activities'] if 'activities' in request.form else []

        sample = model.form_input_to_sample(age, country, industry, role, experience, activities)

        buckets = ['0-10,000', '10,000-20,000', '20,000-30,000', '30,000-40,000', '40,000-50,000',
         '50,000-60,000', '60,000-70,000', '70,000-80,000', '80,000-90,000', '90,000-100,000',
         '100,000-125,000', '125,000-150,000', '150,000-200,000', '200,000-250,000', '>250,000']

        (salary_index, dist) = model.predict(sample)
        return render_template('prediction.html', salary_labels=buckets, salary=buckets[salary_index], salary_distribution=dist)


@app.route('/recommendation', methods=('GET', 'POST'))
def recommendation():
    if request.method == 'GET':
        return render_template('rec_form.html')
    if request.method == 'POST':
        form = request.form.to_dict(flat=False)
        languages = form['regular_languages'] if 'regular_languages' in form else []
        frameworks = form['ml_frameworks'] if 'ml_frameworks' in form else []
        courses = form['online_platforms'] if 'online_platforms' in form else []
        sources = form['media_sources'] if 'media_sources' in form else []
        sample = recom_model.form_input_to_sample(languages, frameworks, courses, sources)
        langs, frameworks, courses, sources = recom_model.get_recommendations(sample, top_n=10)
        langs_keys = [x[0] for x in langs]
        langs_values = [x[1] for x in langs]
        langs_min = min(langs_values)
        langs_values = [x - langs_min + .1 for x in langs_values]
        frameworks_keys = [x[0] for x in frameworks]
        frameworks_values = [x[1] for x in frameworks]
        frameworks_min = min(frameworks_values)
        frameworks_values = [x - frameworks_min + .1 for x in frameworks_values]
        courses_keys = [x[0] for x in courses]
        courses_values = [x[1] for x in courses]
        courses_min = min(courses_values)
        courses_values = [x - courses_min + .1 for x in courses_values]
        sources_keys = [x[0] for x in sources]
        sources_values = [x[1] for x in sources]
        sources_min = min(sources_values)
        sources_values = [x - sources_min + .1 for x in sources_values]
        return render_template('recommendation.html', langs_keys=langs_keys,langs_values=langs_values,
                               frameworks_keys=frameworks_keys,  frameworks_values=frameworks_values,
                               courses_keys=courses_keys, courses_values=courses_values,
                               sources_keys=sources_keys, sources_values=sources_values)


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
