from flask_restful import Resource
from miniagent import api

class TestAPI(Resource):

    def get(self, id):
        return {'result': 'Hello '+str(id)}

api.add_resource(TestAPI, '/test/<int:id>', endpoint='test')

