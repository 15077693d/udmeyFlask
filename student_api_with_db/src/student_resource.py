from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from student_dao import StudentDao
from student import Student

class StudentResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('age', required=True, type=int, help="'age' cannot be left blank")
    parser.add_argument('sex', required=True, help="'sex' cannot be left blank")

    # read the student
    # auth before get method
    @jwt_required()
    def get(self, name):
        the_student = StudentDao.find_by_name(name)
        #the_student = next(filter(lambda student: student['name'] == name, students), None)
        return {"student": the_student}, 200 if the_student else 404

    # add new student
    def post(self, name):
        if StudentDao.find_by_name(name) is not None:
            return {"message": f"the student<{name}> exists"}, 400

        data = StudentResource.parser.parse_args()
        new_student = Student(name, data["sex"], "age": data["age"])
        StudentDao.add(new_student)
        return {"student": new_student}, 201

    # update student
    def put(self, name):
        data = StudentResource.parser.parse_args()
        old_student = next(filter(lambda student: student['name'] == name, students), None)
        if old_student is None:
            new_student = {"name": name, "sex": data["sex"], "age": data["age"]}
            students.append(new_student)
            return {"student": new_student}, 201
        else:
            old_student.update(data)
            return {"message": f"the student<{name}> is updated"}, 200

    # delete student
    def delete(self, name):
        global students
        students = list(filter(lambda student: student['name'] != name, students))
        return {"message": f"the student<{name}> is deleted"}, 200
