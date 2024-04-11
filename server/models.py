# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

 

class User(db.Model, SerializerMixin):
    __tablename__='users'
    

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    registrations = db.relationship('Registration', back_populates='user',  cascade='all, delete-orphan')
    

    events = association_proxy('registrations', 'event',
                                 creator=lambda event_obj: Registration(event=event_obj))
    serialize_rules = ('-registrations.user',)


class Event(db.Model, SerializerMixin):
    __tablename__='events'
    

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    registrations = db.relationship('Registration', back_populates='event',  cascade='all, delete-orphan')
    serialize_rules = ('-registrations.event',)
    users = association_proxy('registrations', 'user', creator=lambda user_obj: Registration(user=user_obj))




class Registration(db.Model,SerializerMixin):
    __tablename__='registrations'

    
    id = db.Column(db.Integer, primary_key=True)
    registration_date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    user= db.relationship('User', back_populates= 'registrations')
    event = db.relationship('Event', back_populates= 'registrations')
    serialize_rules = ('-users.registrations', '-events.registrations',)
