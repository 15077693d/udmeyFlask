from flask import Flask
from flask_jwt import JWT, jwt_required
from flask_restful import Api, Resource, reqparse

"""
 JWT, flask_restful, reqparse
"""

# JWT : json web token -> `show log in
from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'oscar'
api = Api(app)

# /auth
# send username and password
# we send JWT token for next request
jwt = JWT(app, authenticate, identity)

students = [{
    "name": "Mary",
    "sex": "F",
    "age": 10
}]


# 201 -> created
# 202 -> delaying creation
# 404 -> not found
# 400 -> bad request

# assume all student name is unique
class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('age', required=True, type=int, help="'age' cannot be left blank")
    parser.add_argument('sex', required=True, help="'sex' cannot be left blank")

    # read the student
    # auth before get method
    @jwt_required()
    def get(self, name):
        the_student = next(filter(lambda student: student['name'] == name, students), None)
        return {"student": the_student}, 200 if the_student else 404

    # add new student
    def post(self, name):
        if next(filter(lambda student: student['name'] == name, students), None) is not None:
            return {"message": f"the student<{name}> exists"}, 400

        data = Student.parser.parse_args()
        new_student = {"name": name, "sex": data["sex"], "age": data["age"]}
        students.append(new_student)
        return {"student": new_student}, 201

    # update student
    def put(self, name):
        data = Student.parser.parse_args()
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


class Students(Resource):
    # read all student
    def get(self):
        return students


api.add_resource(Student, "/student/<string:name>")
api.add_resource(Students, "/students")

app.run()
