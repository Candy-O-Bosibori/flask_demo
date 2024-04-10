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


# employee_meetings = db.Table(
#     'employees_meetings',
#     metadata,
#     db.Column('employee_id', db.Integer, db.ForeignKey(
#         'employees.id'), primary_key=True),
#     db.Column('meeting_id', db.Integer, db.ForeignKey(
#         'meetings.id'), primary_key=True)
# )

# class Employee(db.Model):
#     __tablename__ = 'employees'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     hire_date = db.Column(db.Date)
#     meetings = db.relationship(
#         'Meeting', secondary=employee_meetings, back_populates='employees')
    
#     assignments = db.relationship(
#         'Assignment', back_populates='employee', cascade='all, delete-orphan')
    
#     projects = association_proxy('assignments', 'project',
#                                  creator=lambda project_obj: Assignment(project=project_obj) )
    
#     def __repr__(self):
#         return f'<Employee {self.id}, {self.name}, {self.hire_date}>'


# class Meeting(db.Model):
#     __tablename__ = 'meetings'

#     id = db.Column(db.Integer, primary_key=True)
#     topic = db.Column(db.String)
#     scheduled_time = db.Column(db.DateTime)
#     location = db.Column(db.String)
#     employees = db.relationship(
#         'Employee', secondary=employee_meetings, back_populates='meetings')
    
    

#     def __repr__(self):
#         return f'<Meeting {self.id}, {self.topic}, {self.scheduled_time}, {self.location}>'


class User(db.Model, SerializerMixin):
    __tablename__='users'
    serialize_rules = ('-registrations.user',)

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    registrations = db.relationship('Registration', back_populates='user',  cascade='all, delete-orphan')

    events = association_proxy('registrations', 'event',
                                 creator=lambda event_obj: Registration(event=event_obj))



class Event(db.Model, SerializerMixin):
    __tablename__='events'
    serialize_rules = ('-registrations.event',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    registrations = db.relationship('Registration', back_populates='event',  cascade='all, delete-orphan')

    users = association_proxy('registrations', 'user', creator=lambda user_obj: Registration(user=user_obj))




class Registration(db.Model,SerializerMixin):
    __tablename__='registrations'

    serialize_rules = ('-users.registrations', '-events.registrations',)
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    user= db.relationship('User', back_populates= 'registrations')
    event = db.relationship('Event', back_populates= 'registrations')
