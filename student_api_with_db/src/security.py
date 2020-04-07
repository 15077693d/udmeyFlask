from werkzeug.security import safe_str_cmp

from user_dao import UserDao

"""
1. when it go to end point /auth
2. method authenticate arg username and password
3. compare password and return user
"""


def authenticate(username, password):
    user = UserDao.find_by_username(username)
    # it can get with defualt value
    if user and safe_str_cmp(user.password, password):
        return user


"""
1. when it go to end point /student/<name> @jwt_required
2. get the payload by jwt {lat,lng, id}
3. return user
"""


# payload -> content of JWT token
def identity(payload):
    user_id = payload['identity']
    user = UserDao.find_by_id(user_id)
    return user


if __name__ == '__main__':
    print(authenticate("oscar", "123"))
