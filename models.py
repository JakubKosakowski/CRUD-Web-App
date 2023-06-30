from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SurveyModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    height = db.Column(db.Integer())
    gender = db.Column(db.String())
    favorite_color = db.Column(db.String())

    def __init__(self, name, age, height, gender, favorite_color):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        self.favorite_color = favorite_color

    def __repr__(self):
        return f"{self.name}"
