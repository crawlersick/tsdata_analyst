from flask_restful import reqparse, abort, Api, Resource


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        TODOS={}
        parser = reqparse.RequestParser()
        parser.add_argument('task', type=str)
        args = parser.parse_args()
        todo_id = '111'
        print(args)
        TODOS[todo_id] = args['task']
        return TODOS, 200
