from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

school = [{
    "name": "Mary",
    "sex": "F",
    "age": 10
}]


# 201 -> created
# 202 -> delaying creation
# 404 -> not found
# 400 -> some problem

# assume all student name is unique
class Student(Resource):
    # read the student
    def get(self, name):
        the_student = next(filter(lambda student: student['name'] == name, school), None)
        return {"student": the_student}, 200 if the_student else 404

    # add new student
    def post(self, name):
        new_student = request.get_json(silent=True)
        the_student = next(filter(lambda student: student['name'] == name, school), None)
        if the_student is not None:
            return {"message": f"the student<{name}> exists"}, 400
        else:
            school.append(new_student)
            return new_student, 201

    # update student
    def put(self, name):
        new_student = request.get_json(silent=True)
        old_student = next(filter(lambda student: student['name'] == name, school))
        if old_student is None:
            school.append(new_student)
            return new_student, 201
        else:
            school.remove(old_student)
            school.append(new_student)
            return new_student, 200

    # delete student
    def delete(self, name):
        the_student = next(filter(lambda student: student['name'] == name, school))
        if the_student is None:
            return {"message": f"the student<{name}> does not exist"}, 400
        else:
            school.remove(the_student)
            return school, 200


class Students(Resource):
    # read all student
    def get(self):
        return school


api.add_resource(Student, "/student/<string:name>")
api.add_resource(Students, "/students")

if __name__ == '__main__':
    app.run()
