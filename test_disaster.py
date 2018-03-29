"""Unit testing for Disaster app"""

import unittest
import app
import model

class TestDisaster(unittest.TestCase):

    def setUp(self):
        """setup testing environment"""
        self.client = app.app.test_client()
        app.app.config['TESTING'] = True

        # Connect to test database
        db(app, "postgresql:///testdb")
        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """cleanup after testing"""
        db.session.close()
        db.drop_all()

    def test_index(self):
        result = client.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
