from flask import Flask, render_template, request, url_for, redirect, flash, get_flashed_messages
from models import db, SurveyModel

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_request
def create_table():
    db.create_all()


@app.route('/')
def home():
    surveys = SurveyModel.query.all()
    return render_template('home.html', surveys=surveys)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Add new survey

        Returns:
        add.html if method is GET
        add record to database and redirect to home page if method is POST

        """
    if request.method == 'GET':
        return render_template('form.html', form_type="add", title="Add new survey")
    else:
        name = request.form.get('name')
        age = request.form.get('age')
        height = request.form.get('height')
        gender = request.form.get('gender')
        fav_color = request.form.get('favorite_color')
        if int(age) < 0:
            flash("Age cannot be lower then 0!")
        if int(height) < 0:
            flash("Height cannot be lower then 0!")
        if any(char.isdigit() for char in name):
            flash("Name cannot contain any numbers!")
        messages = get_flashed_messages()
        if messages:
            return render_template('add.html', form_type="add", title="Add new survey")
        survey = SurveyModel(name=name, age=age, height=height, gender=gender, favorite_color=fav_color)
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('home'))

@app.route('/details/<int:id>')
def details(id):
    """Show details of selected survey

    Parameters:
    id (int): ID of database record

    Returns:
    details.html page

    """
    survey = SurveyModel.query.filter_by(id=id).first()
    return render_template('details.html', survey=survey)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Edit selected survey

        Parameters:
        id (int): ID of database record

        Returns:
        home page with edited record

        """
    survey = SurveyModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if survey:
            if int(request.form.get('age')) < 0:
                flash("Age cannot be lower then 0!")
            if int(request.form.get('height')) < 0:
                flash("Height cannot be lower then 0!")
            if any(char.isdigit() for char in request.form.get('name')):
                flash("Name cannot contain any numbers!")
            messages = get_flashed_messages()
            if messages:
                return render_template('form.html', form_type="edit", title="Edit existed survey", survey=survey)
            survey.name = request.form.get('name')
            survey.age = request.form.get('age')
            survey.height = request.form.get('height')
            survey.gender = request.form.get('gender')
            survey.fav_color = request.form.get('favorite_color')
            db.session.commit()
            return redirect(url_for('details', id=id))
        return f'Survey with id = {id} does not exist'
    return render_template('form.html', form_type="edit", title="Edit existed survey", survey=survey)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """Delete record from database

        Parameters:
        id (int): ID of database record

        Returns:
        redirect to home page after deleting

        """
    survey = SurveyModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if survey:
            db.session.delete(survey)
            db.session.commit()
            return redirect(url_for('home'))
        return f"This survey is already deleted or this survey never existed"
    return render_template('delete.html')


if __name__ == "__main__":
    app.run(debug=True)
