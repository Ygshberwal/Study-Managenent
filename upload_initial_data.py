from main import app
from application.models import db, Role

with app.app_context():
    db.create_all()
    admin=Role(id='admin', name="Admin", description="Admin Description")
    db.session.add(admin)
    stud=Role(id='stud', name="Student", description="Student Description")
    db.session.add(stud)
    inst=Role(id='inst', name="Instructor", description="Instructor Description")
    db.session.add(inst)

    try:
        db.session.commit()
    except:
        print("Database has already been created earlier, try to delete db and run again")