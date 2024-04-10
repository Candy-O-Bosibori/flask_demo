# server/app.py
#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, User, Event, Registration

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)



# get Users 
class Users(Resource):
    def get(self):
        all = User.get.query.all()
        users= [user.to_dict for user in all]
        return make_response(jsonify(users), 200)
    
api.add_resource(Users, '/users')

# get events,post,
class Events(Resource):
    def get(selfs):
        all = Event.get.query.all()
        events= [event.to_dict for event in all]
        return make_response(jsonify(events), 200)
    
    def post(self):
        data = request.get_json()
        new_event = Event(
            
        )
 


# patch ,get, delete events/id
# post registration


if __name__ == '__main__':
    app.run(port=5555, debug=True)