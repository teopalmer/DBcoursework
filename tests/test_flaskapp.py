import unittest, json
#from flask import Flask

#app = Flask(__name__)

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_unauthorized(self):
        response = self.app.get('/authorized')
        
        self.assertEqual(response._status_code,401,'Unauthorized access to page without login')

    def test_multiply(self):
        response = self.app.get('/multiply?x=5&y=7')
        resp = json.loads(response.data.decode())
        self.assertEqual(resp['answer'],35,'Multiply endpoint failed known answer 7*5 = 35')


if __name__ == '__main__':
    print(5)
