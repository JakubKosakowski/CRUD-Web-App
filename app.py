from flask import Flask, render_template, request, url_for
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


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
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
    if request.method == 'GET':
        return render_template('edit.html', person=person)

if __name__ == "__main__":
    app.run(debug=True)