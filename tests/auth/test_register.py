import unittest
import json


from app import create_app
from app.models import db

from app.models.user import User
from tests.config import (
    TEST_VALID_USER,
    TEST_VALID_EMAIL,
    TEST_VALID_PASSWORD,

    TEST_INVALID_USER,
    TEST_INVALID_EMAIL,
    TEST_INVALID_PASSWORD
)

BASE_URL = 'http://127.0.0.1:5000'


class TestRegister(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.client = app.test_client()

        db.app = app

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        data = {
            'fullname': TEST_VALID_USER,
            'email': TEST_VALID_EMAIL,
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/register', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 201)

    def test_not_email_in_register(self):
        data = {
            'fullname': TEST_VALID_USER,
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/register', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 400)

    def test_not_valid_email_in_register(self):
        data = {
            'fullname': TEST_VALID_USER,
            'password': TEST_VALID_PASSWORD,
            'email': TEST_INVALID_EMAIL
        }
        response = self.client.post(
            '/register', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 400)

    def test_user_already_exists_in_register(self):
        user = User(fullname=TEST_VALID_USER,
                    email=TEST_VALID_EMAIL,
                    password=TEST_VALID_PASSWORD)
        db.session.add(user)
        db.session.commit()

        data = {
            'fullname': TEST_VALID_USER,
            'email': TEST_VALID_EMAIL,
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/register', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 409)

    def test_not_fullname_in_register(self):
        data = {
            'email': TEST_VALID_EMAIL,
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/register', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 400)

    def test_not_empty_fullname_in_register(self):
        data = {
            'fullname': '',
            'email': TEST_VALID_EMAIL,
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/register', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 400)

    def test_not_empty_email_in_register(self):
        data = {
            'fullname': TEST_VALID_USER,
            'email': '',
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/register', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 400)

    def test_not_long_password_in_register(self):
        """
        password must be at least 8 chars long
        """
        data = {
            'fullname': TEST_VALID_USER,
            'email': TEST_VALID_EMAIL,
            'password': TEST_INVALID_PASSWORD
        }
        response = self.client.post(
            '/register', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
