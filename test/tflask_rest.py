from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.errorhandler(500)
def error_handling_500(error):
    return jsonify({'error': "Internal Server Error"}, 500)

class TodoSimple(Resource):
    def get(self, todo_id):
        raise TypeError("Some Exception...")
        return {todo_id: todo_id}

api.add_resource(TodoSimple, '/<string:todo_id>')

@app.route('/')
def hello_world():
    raise TypeError("Some Exception...")
    return 'hello world'


if __name__ == '__main__':

    #with app.app_context():
        # within this block, current_app points to app.
    #    print ('OUT ###')
    #    print (talk.sayhello)

    app.run(host="0.0.0.0", port=8808, debug=False, use_reloader=False)
