import unittest
import json
import datetime


from app import create_app
from app.models import db

from app.models.user import User
from app.models.category import Category
from app.models.expense import Expense
from tests.config import (
    TEST_VALID_USER,
    TEST_VALID_EMAIL,
    TEST_VALID_PASSWORD,

    TEST_INVALID_USER,
    TEST_INVALID_EMAIL,
    TEST_INVALID_PASSWORD,
    TEST_VALID_CATEGORY_NAME,
    TEST_INVALID_CATEGORY_NAME,
    TEST_VALID_EXPENSE_NAME,
    TEST_VALID_EXPENSE_AMOUNT,

    TEST_INVALID_EXPENSE_NAME,
    TEST_INVALID_NEGATIVE_EXPENSE_AMOUNT,
    TEST_INVALID_TEXT_EXPENSE_AMOUNT
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

        self.category = Category(label=TEST_VALID_CATEGORY_NAME,
                                 user_id=self.user.id)

        db.session.add(self.category)
        db.session.commit()

        self.TEST_CATEGORY_ID = self.category.id

        with app.test_request_context():
            self.tokens = {
                "access_token": create_access_token(identity=self.user.email),
                "refresh_token": create_refresh_token(identity=self.user.email)
            }

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_expense(self):

        data = {
            "name": TEST_VALID_EXPENSE_NAME,
            'amount': TEST_VALID_EXPENSE_AMOUNT,
            'category_id': self.TEST_CATEGORY_ID

        }

        access_token = self.tokens['access_token']
        response = self.client.post('/expense',
                                    data=json.dumps(data),
                                    content_type='application/json',
                                    headers={
                                        'Authorization': f'Bearer {access_token}'}
                                    )

        self.assertEqual(response.status_code, 201)

    def test_create_invalid_negative_expense(self):

        data = {
            "name": TEST_VALID_EXPENSE_NAME,
            'amount': TEST_INVALID_NEGATIVE_EXPENSE_AMOUNT,
            'category_id': self.TEST_CATEGORY_ID

        }

        access_token = self.tokens['access_token']
        response = self.client.post('/expense',
                                    data=json.dumps(data),
                                    content_type='application/json',
                                    headers={
                                        'Authorization': f'Bearer {access_token}'}
                                    )

        self.assertEqual(response.status_code, 400)

    def test_get_expenses_with_expenses(self):
        """
        Not empty returned array
        """
        data = {
            "name": TEST_VALID_EXPENSE_NAME,
            'amount': TEST_VALID_EXPENSE_AMOUNT,
            'category_id': self.TEST_CATEGORY_ID

        }
        access_token = self.tokens['access_token']
        response = self.client.post('/expense',
                                    data=json.dumps(data),
                                    content_type='application/json',
                                    headers={
                                        'Authorization': f'Bearer {access_token}'}
                                    )

        get_request = self.client.get('/expense',

                                      content_type='application/json',
                                      headers={
                                          'Authorization': f'Bearer {access_token}'}
                                      )

        response_payload = json.loads(get_request.get_data())

        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        expense_representation = {'expenses': [{'amount': 10.03, 'category_id': 1, 'date': current_date, 'id': 1, 'month_id': 201821,
                                                'name': 'Beer', 'user_id': 1}], 'has_next': False, 'has_prev': False, 'next_num': None, 'pages': 1, 'prev_num': None}

        self.assertEqual(response_payload, expense_representation)
