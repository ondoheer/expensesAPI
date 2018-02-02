from app.models.expense import Expense
from app.models.category import Category
from app.models.user import User
from app.models.month import Month


from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
import datetime

main = Blueprint('main', __name__)

@main.route('/main', methods=['GET'])
@jwt_required
def index():

    current_user_email = get_jwt_identity()

    if not current_user_email:
        return jsonify({'error': 'not authorized'}), 401

    user = User.query.filter_by(email=current_user_email).first()


    current_date = datetime.datetime.now()


    # get last 12 months
    last_twelve = Month.get_last_n_months(user.id, 12).all()

    # We prepare the data to be send as JSON
    to_return = {
        'months':[{'{}-{}'.format(month.year, month.month ): {'total':month.total_expenses,
                    'categories': month.expenses_by_category()}} \
                for month in last_twelve ]
    }


    return jsonify(to_return)
