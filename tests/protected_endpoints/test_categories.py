import unittest
import json


from app import create_app
from app.models import db

from app.models.user import User
from app.models.category import Category
from tests.config import (
    TEST_VALID_USER,
    TEST_VALID_EMAIL,
    TEST_VALID_PASSWORD,

    TEST_INVALID_USER,
    TEST_INVALID_EMAIL,
    TEST_INVALID_PASSWORD,
    TEST_VALID_CATEGORY_NAME,
    TEST_INVALID_CATEGORY_NAME
)

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)


class TestCategory(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.client = app.test_client()

        db.app = app

        db.session.remove()
        db.drop_all()
        db.create_all()

        self.user = User(fullname=TEST_VALID_USER,
                         email=TEST_VALID_EMAIL,
                         password=TEST_VALID_PASSWORD)
        db.session.add(self.user)
        db.session.commit()

        with app.test_request_context():
            self.tokens = {
                "access_token": create_access_token(identity=self.user.email),
                "refresh_token": create_refresh_token(identity=self.user.email)
            }

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_category(self):

        data = {
            "label": TEST_VALID_CATEGORY_NAME
        }

        access_token = self.tokens['access_token']
        response = self.client.post('/category',
                                    data=json.dumps(data),
                                    content_type='application/json',
                                    headers={
                                        'Authorization': f'Bearer {access_token}'}
                                    )

        self.assertEqual(response.status_code, 201)

    def test_get_categories_with_categories(self):
        """
        Not empty returned array
        """

        data = {
            "label": TEST_VALID_CATEGORY_NAME
        }

        access_token = self.tokens['access_token']
        response = self.client.post('/category',
                                    data=json.dumps(data),
                                    content_type='application/json',
                                    headers={
                                        'Authorization': f'Bearer {access_token}'}
                                    )

        get_request = self.client.get('/category',

                                      content_type='application/json',
                                      headers={
                                          'Authorization': f'Bearer {access_token}'}
                                      )

        category_representation = [
            {'id': 1, 'label': 'Compras', 'name': 'compras', 'user_id': 1}]
        response_payload = json.loads(get_request.get_data())

        self.assertEqual(get_request.status_code, 200)
        self.assertEqual(category_representation, response_payload)
