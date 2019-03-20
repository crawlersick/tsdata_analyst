from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from app.batchwatcher import a1
app = Flask(__name__)
api = Api(app)
api.add_resource(a1.HelloWorld,'/')
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
