from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "test_key"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

class HelloWord(Resource):
    @jwt_required()
    def get(self):
        return {"secretpage":"secretinfo"}, 200

api.add_resource(HelloWord, "/")


if __name__ == '__main__':
    app.run(debug=True)
