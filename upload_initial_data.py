from main import app, datastore 
from application.models import db, Role

with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name="admin", description="User is an admin")
    datastore.find_or_create_role(name="inst", description="User is an Instructor")
    datastore.find_or_create_role(name="stud", description="User is a Student") 
    try:
        db.session.commit()
    except:
        print("session is not committed")

    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(email="admin@email.com", password="admin", roles=["admin"], fs_uniquifier="some_value")
    if not datastore.find_user(email="inst1@email.com"):
        datastore.create_user(email="inst1@email.com", password="inst1",roles=["inst"], active=False)
    if not datastore.find_user(email="stud1@email.com"):
        datastore.create_user(email="stud1@email.com", password="studl", roles=["stud"], fs_uniquifier="some_value1")
    db.session.commit()