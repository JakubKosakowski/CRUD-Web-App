from flask import Flask, render_template, request, url_for, redirect
from database_execute import exec_sql

app = Flask(__name__)


@app.route('/')
def home():
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
            'favorite_color': data[4]
        }
        people.append(temp)

    return render_template('home.html', people=people)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        age = request.form.get('age')
        height = request.form.get('height')
        gender = request.form.get('gender')
        fav_color = request.form.get('favorite_color')
        exec_sql("""
            INSERT INTO People(age, height, gender, favorite_color)
            VALUES (?, ?, ?, ?);
        """, (age, height, gender, fav_color))
        return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
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
            'favorite_color': data[0][4]
        }
        return render_template('edit.html', person=person)
    else:
        age = request.form.get('age')
        height = request.form.get('height')
        gender = request.form.get('gender')
        fav_color = request.form.get('favorite_color')
        exec_sql("""
                    UPDATE People
                    SET age = ?, height = ?, gender = ?, favorite_color = ?
                    WHERE id = ?
                """, (age, height, gender, fav_color, id))
        return redirect(url_for('home'))


@app.route('/delete/<int:id>')
def delete(id):
    exec_sql("""
        DELETE FROM People WHERE id = ?;
    """, (id,))
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)