from flask import Flask, render_template, request, url_for, redirect
from database_execute import exec_sql

app = Flask(__name__)


@app.route('/')
def home():
    """Show all surveys in database

    Returning:
    Home page with all surveys

    """
    datas = exec_sql(
        """
        SELECT * FROM People;
        """
    )
    people = list()
    for data in datas:
        temp = {
            'id': data[0],
            'age': data[1],
            'height': data[2],
            'gender': data[3],
            'favorite_color': data[4],
            'name': data[5]
        }
        people.append(temp)

    return render_template('home.html', people=people)


@app.route('/details/<int:id>')
def details(id):
    """Show details of selected survey

    Parameters:
    id (int): ID of database record

    Returns:
    details.html page

    """
    data = exec_sql("""
                    SELECT * FROM People
                    WHERE id = ?;
                """, (id,))
    person = {
        'id': data[0][0],
        'age': data[0][1],
        'height': data[0][2],
        'gender': data[0][3],
        'favorite_color': data[0][4],
        'name': data[0][5]
    }
    return render_template('details.html', person=person)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Add new survey

        Returns:
        add.html if method is GET
        add record to database and redirect to home page if method is POST

        """
    if request.method == 'GET':
        return render_template('add.html')
    else:
        name = request.form.get('name')
        age = request.form.get('age')
        height = request.form.get('height')
        gender = request.form.get('gender')
        fav_color = request.form.get('favorite_color')
        exec_sql("""
            INSERT INTO People(age, height, gender, favorite_color, name)
            VALUES (?, ?, ?, ?, ?);
        """, (age, height, gender, fav_color, name))
        return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Edit selected survey

        Parameters:
        id (int): ID of database record

        Returns:
        home page with edited record

        """
    if request.method == 'GET':
        data = exec_sql("""
                SELECT * FROM People
                WHERE id = ?;
            """, (id,))
        person = {
            'id': data[0][0],
            'age': data[0][1],
            'height': data[0][2],
            'gender': data[0][3],
            'favorite_color': data[0][4],
            'name': data[0][5]
        }
        return render_template('edit.html', person=person)
    else:
        name = request.form.get('name')
        age = request.form.get('age')
        height = request.form.get('height')
        gender = request.form.get('gender')
        fav_color = request.form.get('favorite_color')
        exec_sql("""
                    UPDATE People
                    SET age = ?, height = ?, gender = ?, favorite_color = ?, name = ?
                    WHERE id = ?
                """, (age, height, gender, fav_color, name, id))
        return redirect(url_for('home'))


@app.route('/delete/<int:id>')
def delete(id):
    """Delete record from database

        Parameters:
        id (int): ID of database record

        Returns:
        redirect to home page after deleting

        """
    exec_sql("""
        DELETE FROM People WHERE id = ?;
    """, (id,))
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
