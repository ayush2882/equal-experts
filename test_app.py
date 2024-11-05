import unittest
import app

class TestGistAPI(unittest.TestCase):
    
    def setUp(self):
        app.app.testing = True
        self.client = app.app.test_client()

    def test_get_gists_for_valid_user(self):
        """To test a valid GitHub user(/octocat)"""
        response = self.client.get('/octocat')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
    
    def test_get_gists_for_invalid_user(self):
        """To test an invalid GitHub user"""
        response = self.client.get('/nonexistentuser')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)
    
if __name__ == '__main__':
    unittest.main()