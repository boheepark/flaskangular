import json

from asdf.tests.base import BaseTestCase

class TestAuthService(BaseTestCase):

    def test_signup(self):
        with self.client:
            res = self.client.post("/auth/signup", data=json.dumps(dict(
                uname="test",
                name="test",
                email="email@test.com",
                pw="TestPa$$3121",
                checking=100000,
                trading=100000,
                gender="male",
                phone="1234567890",
                addr="1234 Main St.",
                town="Fort Lee",
                state="NJ",
                zip="07024"
            )),
            content_type="application/json")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 201)
            self.assertIn("success", data["status"])
            res = self.client.get("/api/user/unames")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 200)
            self.assertIn("test", data["data"])

    def test_signup_empty(self):
        with self.client:
            res = self.client.post("/auth/signup", data=json.dumps(dict()), content_type="application/json")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertIn("Empty payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_signup_incomplete(self):
        with self.client:
            res = self.client.post("/auth/signup", data=json.dumps(dict(
                uname="test",
                name="test",
                email="email@test.com",
                pw="TestPa$$3121"
            )),
            content_type="application/json")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertIn("Incomplete payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_signup_duplicate_uname(self):
        with self.client:
            self.client.post("/auth/signup", data=json.dumps(dict(
                uname="test",
                name="test",
                email="email@test.com",
                pw="TestPa$$3121",
                checking=100000,
                trading=100000,
                gender="male",
                phone="1234567890",
                addr="1234 Main St.",
                town="Fort Lee",
                state="NJ",
                zip="07024"
            )),
            content_type="application/json")
            res = self.client.post("/auth/signup", data=json.dumps(dict(
                uname="test",
                name="test2",
                email="email2@test.com",
                pw="TestPa$$3121",
                checking=100000,
                trading=100000,
                gender="male",
                phone="1234567890",
                addr="1234 Main St.",
                town="Fort Lee",
                state="NJ",
                zip="07024"
            )),
            content_type="application/json")
            data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertIn("fail", data["status"])

        def test_signup_duplicate_email(self):
            with self.client:
                self.client.post("/auth/signup", data=json.dumps(dict(
                    uname="test",
                    name="test",
                    email="email@test.com",
                    pw="TestPa$$3121",
                    checking=100000,
                    trading=100000,
                    gender="male",
                    phone="1234567890",
                    addr="1234 Main St.",
                    town="Fort Lee",
                    state="NJ",
                    zip="07024"
                )),
                content_type="application/json")
                res = self.client.post("/auth/signup", data=json.dumps(dict(
                    uname="test2",
                    name="test2",
                    email="email@test.com",
                    pw="TestPa$$3121",
                    checking=100000,
                    trading=100000,
                    gender="male",
                    phone="1234567890",
                    addr="1234 Main St.",
                    town="Fort Lee",
                    state="NJ",
                    zip="07024"
                )),
                content_type="application/json")
                data = json.loads(res.data.decode())
                self.assertEqual(res.status_code, 400)
                self.assertIn("fail", data["status"])

        def test_signin(self):
            with self.client:
                self.client.post("/auth/signup", data=json.dumps(dict(
                    uname="test",
                    name="test",
                    email="email@test.com",
                    pw="TestPa$$3121",
                    checking=100000,
                    trading=100000,
                    gender="male",
                    phone="1234567890",
                    addr="1234 Main St.",
                    town="Fort Lee",
                    state="NJ",
                    zip="07024"
                )),
                content_type="application/json")
                res = self.client.post("/auth/signin", data=json.dumps(dict(
                    uname="test",
                    pw="TestPa$$3121"
                )),
                content_type="application/json")
                data = json.loads(res.data.decode())
                self.assertEqual(res.status_code, 200)
                self.assertIn("success", data["status"])
