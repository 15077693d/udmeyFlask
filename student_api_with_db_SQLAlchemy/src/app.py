from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.student_resource import StudentResource, StudentsResource
from resources.user_resource import UserResource
from resources.school_resource import SchoolsResource, SchoolResource
from db import db

"""
 JWT, flask_restful, reqparse
"""

# JWT : json web token -> `show log in
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'oscar'
api = Api(app)

# /auth
# send username and password
# we send JWT token for next request
jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_table():
    db.create_all()


# 201 -> created
# 202 -> delaying creation
# 404 -> not found
# 400 -> bad request
api.add_resource(StudentResource, "/student/<string:name>")
api.add_resource(StudentsResource, "/students")
api.add_resource(UserResource, "/user/<string:username>")
api.add_resource(SchoolResource, "/school/<string:name>")
api.add_resource(SchoolsResource, "/schools")

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
