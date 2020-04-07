from flask_restful import Resource, reqparse

from user_dao import UserDao


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True, help="'username' cannot be blank！")
    parser.add_argument("password", required=True, help="'password' cannot be blank！")

    def post(self):
        data = UserResource.parser.parse_args()
        UserDao.add(data['username'], data['password'])
        return data
