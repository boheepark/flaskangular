import json

from asdf.tests.base import BaseTestCase

class TestAuthService(BaseTestCase):

    def test_signup(self):
        with self.client:
            res = self.client.post("/auth/signup", data=json.dumps(dict(
                uname="uname",
                name="name",
                email="email@test.com",
                pw="Left3.5Right3.75",
                checking=100000,
                trading=100000,
                gender="male",
                phone="1234567890",
                addr="1234 Main St.",
                town="NYC",
                state="NY",
                zip="12345"
            )),
            content_type="application/json")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 201)
            # self.assertIn("email@test.com")
