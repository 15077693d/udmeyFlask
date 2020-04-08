from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from Entity.student import Student
from Dao.student_dao import StudentDao


class StudentResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('age', required=True, type=int, help="'age' cannot be left blank")
    parser.add_argument('sex', required=True, help="'sex' cannot be left blank")

    # read the student
    # auth before get method
    @jwt_required()
    def get(self, name):
        the_student = StudentDao.find_by_name(name)
        # the_student = next(filter(lambda student: student['name'] == name, students), None)
        return {"student": the_student}, 200 if {"message": f"the student<{name}> is not found"} else 404

    # add new student
    def post(self, name):
        if StudentDao.find_by_name(name):
            return {"message": f"the student<{name}> exists"}, 400

        data = StudentResource.parser.parse_args()
        new_student = Student(name, data["sex"], data["age"])
        StudentDao.add(new_student)
        return {"student": new_student}, 201

    # update student
    def put(self, name):
        data = StudentResource.parser.parse_args()
        old_student = StudentDao.find_by_name(name)
        new_student = Student(name, data["sex"], data["age"])
        if old_student is None:
            StudentDao.add(new_student)
            return {"student": new_student}, 201
        else:
            StudentDao.update(new_student)
            return {"message": f"the student<{name}> is updated"}, 200

    # delete student
    def delete(self, name):
        StudentDao.delete(name)
        return {"message": f"the student<{name}> is deleted"}, 200
