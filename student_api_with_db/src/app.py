from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from Resource.student_resource import StudentResource
from Resource.students_resource import StudentsResource
from Resource.user_resource import UserResource

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

# 201 -> created
# 202 -> delaying creation
# 404 -> not found
# 400 -> bad request
api.add_resource(StudentResource, "/student/<string:name>")
api.add_resource(StudentsResource, "/students")
api.add_resource(UserResource, "/user/<string:username>")

app.run(debug=True)
