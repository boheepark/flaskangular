from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import unittest

from asdf import create_app, db

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

@manager.command
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('asdf/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def seed_db():
    db.session.add(User(None,"test","name","test@asdf.com","TestPa$$3121",100000,100000,"male","1234567890","123 Main St.","Fort Lee","NJ","07024",None,None,None,None))
    db.session.add(User(None,"test2","name2","test2@asdf.com","TestPa$$3121",100000,100000,"male","1234567890","123 Main St.","Fort Lee","NJ","07024",None,None,None,None))
    db.session.add(User(None,"test3","name3","test3@asdf.com","TestPa$$3121",100000,100000,"male","1234567890","123 Main St.","Fort Lee","NJ","07024",None,None,None,None))
    db.session.commit()

if __name__ == "__main__":
    manager.run()
