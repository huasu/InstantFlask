from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


engine = create_engine('sqlite:///sched.db', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

now = datetime.now()

session.add(Appointment(
    title='Important Meeting',
    start=now + timedelta(days=3),
    end=now + timedelta(days=3, seconds=3600),
    allday=False,
    location='The Office'))
session.commit()

session.add(Appointment(
    title='Past Meeting',
    start=now - timedelta(days=3),
    end=now - timedelta(days=3, seconds=3600),
    allday = False,
    location='The Office'))
session.commit()

session.add(Appointment(
    title='Follow up',
    start=now + timedelta(days=4),
    end=now + timedelta(days=4, seconds=3600),
    allday=False,
    location='The Office'))
session.commit()

session.add(Appointment(
    title='Day Off',
    start=now - timedelta(days=5),
    end=now - timedelta(days=5),
    allday = True))
session.commit()

# Create
appt = Appointment(
    title = 'My Appointment',
    start = now,
    end = now + timedelta(seconds=1800),
    allday = False)
session.add(appt)
session.commit()

# Update
appt.title = 'Your Appointment'
session.commit()

# Delete
session.delete(appt)
session.commit()

# Get an appointment by ID.
appt = session.query(Appointment).get(1)
print(appt)

# Get all appointments.
appts = session.query(Appointment).all()
print(appts)

# Get all appointments before right now, after right not.
appts = session.query(Appointment).filter(Appointment.start < datetime.now()).all()
print(appts)
appts = session.query(Appointment).filter(Appointment.start >= datetime.now()).all()
print(appts)

# Get all appointments before a certain date
appts = session.query(Appointment).filter(Appointment.start <= datetime(2013, 5, 1)).all()
print(appts)

# Get the first appointment matching the filter query
appts = session.query(Appointment).filter(Appointment.start <= datetime(2013, 5, 1)).first()
print(appts)

