import sqlite3
from db import db


class Student(db.Model):
    __tablename__ = 'student'
    name = db.Column(db.String(80), primary_key=True)
    sex = db.Column(db.String(80))
    age = db.Column(db.Integer)
    school_name = db.Column(db.String(80), db.ForeignKey('school.name'))
    school = db.relationship('School')

    # id is python keyword
    def __init__(self, name, sex, age, school_name):
        self.name = name
        self.sex = sex
        self.age = age
        self.school_name = school_name

    def __str__(self):
        return f"<name: {self.name} sex: {self.sex} age: {self.age}>"

    def json(self):
        return {"name": self.name,
                "sex": self.sex,
                "age": self.age,
                "school_name": self.school_name}

    @classmethod
    def find_all(cls):
        students = cls.query.all()
        return [student.json() for student in students]

    @classmethod
    def find_by_name(cls, name):
        student = cls.query.filter_by(name=name).first()
        if student:
            return student.json()
        else:
            return None

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        student = self.query.filter_by(name=self.name).first()
        student.sex = self.sex
        student.age = self.age
        db.session.commit()

    @classmethod
    def delete(cls, name):
        cls.query.filter_by(name=name).delete()
        db.session.commit()
