from flask import jsonify
from flask_api import status
from flask_restful import Resource, reqparse
from .executer import Executer

class Command(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('command_name', type=str)
    parser.add_argument('key', type=str)
    parser.add_argument('items', type=list, location='json')

    def get(self, command_name):
        return dict(command_name=command_name), status.HTTP_200_OK

    def post(self):
        data = Command.parser.parse_args()
        print(data)
        print(Executer.instance().test())
        return dict(message='OK'), status.HTTP_200_OK