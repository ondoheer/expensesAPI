from app.models.expense import Expense
from app.models.category import Category
from app.models.user import User


from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
import datetime

main = Blueprint('main', __name__)

@main('/main', methods=['GET'])
@jwt_required
def main():

    current_user = get_jwt_identity()

    if not current_user:
        return jsonify({'error': 'not authorized'}), 401

    user = User.query.filter_by(email=current_user).first()


    current_date = datetime.datetime.now()

