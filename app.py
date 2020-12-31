from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def new_cv():
    return render_template('New-cv.html')


@app.route('/aboutmyself')
def about_myself():
    return render_template('About Myself.html')


@app.route('/academiceducation')
def academic_education():
    return render_template('Academic Education.html')


@app.route('/academicknowledge')
def academic_knowledge():
    return render_template('Academic Knowledge.html')


@app.route('/army')
def army():
    return render_template('Army.html')


@app.route('/contactme')
def contact_me():
    return render_template('Contact me.html')


@app.route('/highschoolgraduation')
def high_school_graduation():
    return render_template('Highschool Gradiation.html')


@app.route('/insummery')
def in_summery():
    return render_template('In Summery.html')


@app.route('/jobs')
def jobs():
    return render_template('Jobs.html')


@app.route('/recommendations')
def recommendations():
    return render_template('Recomendations.html')


@app.route('/block')
def block():
    return render_template('Block.html')


@app.route('/hobbies')
def assignment8():
    return render_template('Assignment 8.html', title='', user={'firstname': "Noam", 'lastname': "Shachar"}
                           , hobbies=('Basketball', 'Football', 'WEB', 'Swimming', 'Piano'))


if __name__ == '__main__':
    app.run(debug=True)
