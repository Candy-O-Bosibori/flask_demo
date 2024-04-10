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
    
    db.session.add_all([u1, u2, u3])
    db.session.commit()

    # Add projects
    e1= Event(title="sip and paint",  location= "Riara")
    e2 = Event(title="Girls day out", location= "Maji matamu")
    e3 = Event(title="biking", location= "ruiru")
    
    db.session.add_all([e1,e2,e3])
    db.session.commit()

   
    r1 = Registration(
                    registration_date=datetime.datetime(2023, 5, 28),
                    user=u1,
                    event=e1)
    r2 = Registration(
                    registration_date=datetime.datetime(2023, 6, 10),
                    
                    user=u2,
                    event=e2)
    r3 = Registration(
                    registration_date=datetime.datetime(2023, 11, 1),
                    
                    user=u2,
                    event=e3)

    db.session.add_all([r1,r2,r3])
    db.session.commit()


    pass