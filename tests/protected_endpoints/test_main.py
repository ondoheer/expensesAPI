import unittest
import json


from app import create_app
from app.models import db

from app.models.user import User
from app.models.category import Category
from app.models.expense import Expense
from app.models.month import Month

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
    TEST_VALID_MONTH_ID,
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

        self.month = Month(
            user_id=self.user.id,
            year_month_usr=TEST_VALID_MONTH_ID
        )

        db.session.add(self.month)
        db.session.commit()

        self.expense = Expense(
            name=TEST_VALID_EXPENSE_NAME,
            amount=TEST_VALID_EXPENSE_AMOUNT,
            category_id=self.category.id,
            user_id=self.user.id,
            month_id=TEST_VALID_MONTH_ID
        )

        db.session.add(self.expense)
        db.session.commit()

        with app.test_request_context():
            self.tokens = {
                "access_token": create_access_token(identity=self.user.email),
                "refresh_token": create_refresh_token(identity=self.user.email)
            }

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_main_data_with_created_category_and_expenses(self):

        access_token = self.tokens['access_token']
        response = self.client.get('/main',
                                   content_type='application/json',
                                   headers={
                                       'Authorization': f'Bearer {access_token}'}
                                   )

        response_payload = json.loads(response.get_data())

        main_representation = [{'categories': [{'amount': [
            [10.03]], 'id': '1', 'label': 'Compras', 'name': 'compras'}], 'id': '2018-1-1', 'total': 10.03}]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_payload, main_representation)
