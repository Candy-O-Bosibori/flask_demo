import datetime
from app import app
from models import db, Registration, User, Event

with app.app_context():
    
    # Delete all rows in tables
    
    Registration.query.delete()
    User.query.delete()
    Event.query.delete()

    # Add employees
    u1 = User(username="Uri Lee")
    u2 = User(username="andrew")
    u3 = User(username="Judas")
    u4= User(username="John")
    u5 = User(username="Batholomew")
    u6 = User(username="Mathhew")
    u7 = User(username="jude")
    u8 = User(username="zuzu")
    db.session.add_all([u1, u2, u3, u4, u5, u6, u8 , u7])
    db.session.commit()

    # # Add meetings
    # m1 = Meeting(topic="Software Engineering Weekly Update",
    #              scheduled_time=datetime.datetime(
    #                  2023, 10, 31, 9, 30),
    #              location="Building A, Room 142")
    # m2 = Meeting(topic="Github Issues Brainstorming",
    #              scheduled_time=datetime.datetime(
    #                  2023, 12, 1, 15, 15),
    #              location="Building D, Room 430")
    # db.session.add_all([m1, m2])
    # db.session.commit()

    # Add projects
    e1= Event(title="sip and paint",  location= "Riara")
    e2 = Event(title="Girls day out", location= "Maji matamu")
    e3 = Event(title="biking", location= "ruiru")
    e4= Event(title="Subaru racing",location= "Nairobi")
    e5 = Event(title="hunting", location= "Moyale")
    db.session.add_all([e1,e2,e3,e4,e5])
    db.session.commit()

    # Many-to-many relationship between employee and meeting
    # Add meetings to an employee
    # e1.meetings.append(m1)
    # e1.meetings.append(m2)
    # # Add employees to a meeting
    # m2.employees.append(e2)
    # m2.employees.append(e3)
    # m2.employees.append(e4)
    # db.session.commit()

    # Many-to-many relationship between employee and project through assignment
    
    r1 = Registration(
                    start_date=datetime.datetime(2023, 5, 28),
                    end_date=datetime.datetime(2023, 10, 30),
                    user=u1,
                    event=e1)
    r2 = Registration(
                    start_date=datetime.datetime(2023, 6, 10),
                    end_date=datetime.datetime(2023, 10, 1),
                    user=u2,
                    event=e2)
    r3 = Registration(
                    start_date=datetime.datetime(2023, 11, 1),
                    end_date=datetime.datetime(2024, 2, 1),
                    user=u4,
                    event=e5)

    db.session.add_all([r1,r2,r3])
    db.session.commit()


    pass