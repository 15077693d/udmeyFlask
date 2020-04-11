from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.student import Student


class StudentsResource(Resource):
    # read all student
    def get(self):
        students = Student.find_all()
        return students


class StudentResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('age', required=True, type=int, help="'age' cannot be left blank")
    parser.add_argument('sex', required=True, help="'sex' cannot be left blank")
    parser.add_argument('school_name', required=True, help="'school_name' cannot be left blank")

    # read the student
    # auth before get method
    @jwt_required()
    def get(self, name):
        the_student = Student.find_by_name(name)
        return {"student": the_student}, 200 if {"message": f"the student<{name}> is not found"} else 404

    # add new student
    def post(self, name):
        if Student.find_by_name(name):
            return {"message": f"the student<{name}> exists"}, 400

        data = StudentResource.parser.parse_args()
        new_student = Student(name, data["sex"], data["age"], data['school_name'])
        new_student.add()
        return {"message": f"the student<{name}> is added"}, 201

    # update student
    def put(self, name):
        data = StudentResource.parser.parse_args()
        old_student = Student.find_by_name(name)
        new_student = Student(name, data["sex"], data["age"], data['school_name'])
        if old_student is None:
            new_student.add()
            return {"message": f"the student<{name}> is added"}, 201
        else:
            new_student.update()
            return {"message": f"the student<{name}> is updated"}, 200

    # delete student
    def delete(self, name):
        Student.delete(name)
        return {"message": f"the student<{name}> is deleted"}, 200
