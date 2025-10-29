from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
from models import db
db.init_app(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}
    
api.add_resource(HelloWorld, '/message')

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()  # Create database tables for our data models

    app.run(debug=True)