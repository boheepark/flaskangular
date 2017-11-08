from flask_testing import TestCase

from asdf import app, db

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('asdf.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
