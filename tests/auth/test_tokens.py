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


class TestTokens(unittest.TestCase):
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
        response_json = json.loads(response.get_data())
        self.assertIn('access_token', response_json)
        self.assertIn('refresh_token', response_json)

    def test_refresh_token(self):
        data = {
            'email': TEST_VALID_EMAIL,
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/login', content_type='application/json', data=json.dumps(data))
        response_json = json.loads(response.get_data())

        refresh_token = response_json['refresh_token']

        new_response = self.client.post('/refresh',
                                        content_type='application/json',
                                        headers={
                                            'Authorization': f'Bearer {refresh_token}'}
                                        )
        new_response_json = json.loads(new_response.get_data())
        self.assertIn('access_token', new_response_json)
        self.assertNotEqual(
            response_json['access_token'], new_response_json['access_token'])

    def test_invalid_refresh_request(self):

        data = {
            'email': TEST_VALID_EMAIL,
            'password': TEST_VALID_PASSWORD
        }
        response = self.client.post(
            '/login', content_type='application/json', data=json.dumps(data))
        response_json = json.loads(response.get_data())

        refresh_token = response_json['refresh_token']

        new_response = self.client.post('/refresh',
                                        content_type='application/json',
                                        headers={
                                            'Authorization': f'Bearer wrongtoken'}
                                        )
        new_response_json = json.loads(new_response.get_data())

        self.assertEqual(new_response.status_code, 422)
