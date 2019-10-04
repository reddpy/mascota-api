from flask_restful import Resource, Api
from flask_jwt import jwt_required
from flask import jsonify

class HelloWorld(Resource):
    @jwt_required()
    def get(self):
        return {'hello': 'hi'}