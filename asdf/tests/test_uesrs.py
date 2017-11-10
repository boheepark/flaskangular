import json

from asdf.tests.base import BaseTestCase

class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Ensure the /api/user/unames route behaves correctly."""
        res = self.client.get('/api/user/unames')
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertIn('asdf', data['data'])
        self.assertIn('success', data['status'])
