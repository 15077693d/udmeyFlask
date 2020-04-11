from db import db


class School(db.Model):
    __tablename__ = "school"
    name = db.Column(db.String(80), primary_key=True)
    students = db.relationship('Student')

    def __init__(self, name, students=[]):
        self.name = name
        self.students = students

    def json(self):
        return {'name': self.name,
                'student': [student.json() for student in self.students]}

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return {'schools': [school.json() for school in cls.query.all()]}

    def __str__(self):
        return f"<name: {self.name} student_amount: {len(self.students)}>"

    @classmethod
    def find_by_name(cls, name):
        school = cls.query.filter_by(name=name).first()
        if school:
            return school.json()
        else:
            return None
