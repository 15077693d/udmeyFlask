from flask_restful import Resource, reqparse

from Dao.user_dao import UserDao


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True, help="'username' cannot be blank！")
    parser.add_argument("password", required=True, help="'password' cannot be blank！")

    def post(self, username):
        if UserDao.find_by_username(username):
            return {"message": f"the student<{username}> exists"}, 400
        data = UserResource.parser.parse_args()
        UserDao.add(data['username'], data['password'])
        return {"user": data}, 200
