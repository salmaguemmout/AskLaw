import unittest
from flask import Flask
import json
from app import app

class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200, "Index page should load successfully.")
    
    def test_chat(self):
        response = self.app.post('/chat', json={'msg': 'Test message'})
        data = json.loads(response.data)
        self.assertIn('response', data, "Response should contain a 'response' key.")
    
    def test_new_session(self):
        response = self.app.post('/new_session')
        data = json.loads(response.data)
        self.assertIn('session_id', data, "Response should contain a 'session_id' key.")

if __name__ == '__main__':
    unittest.main()
