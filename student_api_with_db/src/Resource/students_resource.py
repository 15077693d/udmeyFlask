from flask_restful import Resource

from Dao.student_dao import StudentDao


class StudentsResource(Resource):
    # read all student
    def get(self):
        students = StudentDao.find_all()
        return students
