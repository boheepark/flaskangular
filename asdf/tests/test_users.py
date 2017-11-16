import json

from asdf import db
from asdf.api.models.user import User
from asdf.tests.base import BaseTestCase


def add_user(uname, name, email, pw, checking, trading, gender, phone, addr, town, state, zip):
    new_user = User(
        id = None,
        uname = uname,
        name = name,
        email = email,
        pw = pw,
        checking = checking,
        trading = trading,
        gender = gender,
        phone = phone,
        addr = addr,
        town = town,
        state = state,
        zip = zip,
        active = None,
        last_seen = None,
        updated_at = None,
        created_at = None
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

class TestUserService(BaseTestCase):

    def test_get_unames(self):
        add_user("test", "test", "test@asdf.com", "TestPa$$3121", 100000, 100000, "male", "1234567890", "1234 Main St.", "Fort Lee", "NJ", "07024")
        add_user("test2", "test2", "test2@asdf.com", "TestPa$$3121", 100000, 100000, "male", "1234567890", "1234 Main St.", "Fort Lee", "NJ", "07024")
        add_user("test3", "test3", "test3@asdf.com", "TestPa$$3121", 100000, 100000, "male", "1234567890", "1234 Main St.", "Fort Lee", "NJ", "07024")
        with self.client:
            res = self.client.get("/api/user/unames")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertIn("success", data["status"])
            self.assertEqual(len(data["data"]), 3)
            self.assertIn("test", data["data"])
            self.assertIn("test2", data["data"])
            self.assertIn("test3", data["data"])

    def test_get_emails(self):
        add_user("test", "test", "test@asdf.com", "TestPa$$3121", 100000, 100000, "male", "1234567890", "1234 Main St.", "Fort Lee", "NJ", "07024")
        add_user("test2", "test2", "test2@asdf.com", "TestPa$$3121", 100000, 100000, "male", "1234567890", "1234 Main St.", "Fort Lee", "NJ", "07024")
        add_user("test3", "test3", "test3@asdf.com", "TestPa$$3121", 100000, 100000, "male", "1234567890", "1234 Main St.", "Fort Lee", "NJ", "07024")
        with self.client:
            res = self.client.get("/api/user/emails")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertIn("success", data["status"])
            self.assertEqual(len(data["data"]), 3)
            self.assertIn("test@asdf.com", data["data"])
            self.assertIn("test2@asdf.com", data["data"])
            self.assertIn("test3@asdf.com", data["data"])
