from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {'test': 'OKAY'}, 200

class HelloWorld(Resource):
    def get(self):
        return {'message': "Hello World"}

api.add_resource(Test,'/test')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port='3000')