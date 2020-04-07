from flask_restful import Resource

from user_dao import UserDao


class StudentsResource(Resource):
    # read all student
    def get(self):
        UserDao.find_all()
        return "students"
