from flask_restful import Resource, reqparse
from models.school import School


class SchoolsResource(Resource):

    def get(self):
        return School.find_all()


class SchoolResource(Resource):
    parser = reqparse.RequestParser()

    def get(self, name):
        school = School.find_by_name(name)
        if school:
            return school, 200
        else:
            return {"message": "school<{}> does not exist".format(name)}, 400

    def post(self, name):
        if School.find_by_name(name):
            return {"message": "school<{}> exist".format(name)}, 400
        else:
            School(name=name).add()
            print(School(name=name))
            return {"message": "school<{}> is added".format(name)}, 201
