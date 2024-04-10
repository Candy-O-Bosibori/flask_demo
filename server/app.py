# server/app.py
#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
import os

from models import db, User, Event, Registration

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

# home
class Home(Resource):
    def get(self):
        return {"message":"this is the home page"}
api.add_resource(Home, '/') 

# get Users 
class Users(Resource):
    def get(self):
        users = [user.to_dict(rules=('-registrations.user', '-registrations.event',)) for user in User.query.all()]
        return make_response(users, 200)
    
api.add_resource(Users, '/users')

# get events,post,
class Events(Resource):
    def get(self):
        all = Event.query.all()
        events= [event.to_dict(rules=('-registrations.user', '-registrations.event',)) for event in all]
        return make_response(jsonify(events), 200)
    
    def post(self):
        data = request.get_json()
        new_event = Event(
            title=data['title'],
            location=data['location']
        )
        db.session.add(new_event)
        db.session.commit()
        return make_response(new_event.to_dict(), 201)
    

api.add_resource(Events, '/events')


# patch ,get, delete events/id
class EventsById(Resource):
    def get(self, id):
        event = Event.query.filter(Event.id == id).first()

        if event is None:
            return make_response({'error': 'Event not found'}, 404)

        return make_response(event.to_dict(rules=('-registrations',)), 200)

    def patch(self, id):
        data = request.get_json()

        event = Event.query.filter_by(id=id).first()

        for attr in data:
            setattr(event, attr, data[attr])

        db.session.add(event)
        db.session.commit()

        return make_response(event.to_dict(rules=('-registrations',)), 200)
    
    def delete(self, id):
        event = Event.query.filter_by(id=id).first()
        db.session.delete(event)
        db.session.commit()

        return make_response('', 204)
        
api.add_resource(EventsById, '/events/<int:id>')  



# get /post registration

class Registrations(Resource):
    def get(self):
        regs= [reg.to_dict(rules=('-user.registrations', '-event.registrations',)) for reg in Registration.query.all()]
        return make_response(jsonify(regs), 200)

    def post(self):
        data = request.get_json()
        new_event = Registration(
            registration_sate=data['registration_date'],
            event=data['event']
        )
        db.session.add(new_event)
        db.session.commit()
        return make_response(new_event.to_dict('-user.registrations', '-event.registrations',), 201)
    

        

api.add_resource(Registrations, '/reg')  


if __name__ == '__main__':
    app.run(port=5555, debug=True)