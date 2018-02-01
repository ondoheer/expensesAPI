from flask import Blueprint, jsonify, abort, g
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import db
from app.models.user import User
from app.models.expense import Expense



expenses = Blueprint("expenses", __name__)

@expenses.route("/expense", methods=["GET"])
@jwt_required
def all():

    current_user = get_jwt_identity()

    if not current_user:
        return jsonify({'error': 'not authorized'}), 401

    user = User.query.filter_by(email=current_user).first()

    expenses = db.session.query(Expense).filter_by(user_id=user.id).all()



    return jsonify({'expenses':Expense.serialize_list(expenses)}), 200





