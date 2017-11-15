import json

from asdf.tests.base import BaseTestCase

class TestUserService(BaseTestCase):

    def test_users(self):
        res = self.client.get('/api/user/unames')
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertIn('success', data['status'])
