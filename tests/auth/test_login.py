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


class TestLogin(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.client = app.test_client()

        db.app = app

        db.create_all()

        user = User(fullname=TEST_VALID_USER,
                    email=TEST_VALID_EMAIL,
                    password=TEST_VALID_PASSWORD)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_user(self):

        data = {
            'email': TEST_VALID_EMAIL,
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/login', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 200)

    def test_not_email_in_login(self):

        data = {
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/login', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 400)

    def test_not_password_in_login(self):

        data = {
            'email': TEST_VALID_EMAIL
        }
        response = self.client.post(
            '/login', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 400)

    def test_validate_password_correct(self):
        data = {
            'email': TEST_VALID_EMAIL,
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/login', content_type='application/json', data=json.dumps(data))

        self.assertEqual(response.status_code, 200)

    def test_validate_password_correct(self):

        self.assertTrue(User.validate_password(
            TEST_VALID_EMAIL, TEST_VALID_PASSWORD))

    def test_validate_password_correct(self):

        self.assertFalse(User.validate_password(
            TEST_VALID_EMAIL, TEST_INVALID_PASSWORD))


if __name__ == '__main__':
    unittest.main()
