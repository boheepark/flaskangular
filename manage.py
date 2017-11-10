from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import unittest

from asdf import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
@manager.command
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('asdf/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
if __name__ == "__main__":
    manager.run()
