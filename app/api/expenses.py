from flask import Blueprint, jsonify, abort, g, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm.exc import NoResultFound

from app.models import db
from app.models.user import User
from app.models.expense import Expense
from app.models.month import Month



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




@expenses.route("/expense", methods=['POST'])
@jwt_required
def create():

    current_user = get_jwt_identity()

    if not current_user:
        return jsonify({'error': 'not authorized'}), 401

    user = User.query.filter_by(email=current_user).first()

    params = request.get_json()
    amount = params.get('amount', None)
    name = params.get('name', None)
    category_id = params.get('category_id', None)

    # This ought to be better validated
    if not amount or not name or not category_id:
        return jsonify({"msg": "Bad request"}), 400

    new_expense = Expense(
        name=name,
        amount=amount,
        category_id=category_id,
        user_id=user.id
    )

    month_code = Month.build_user_month_code(user.id)
    try:
        month = db.session.query(Month).filter(
            Month.year_month_usr == month_code
        ).one()
    except NoResultFound:

        month = Month(year_month_usr=month_code, user_id=user.id)
    # new expense for the month
    month.expenses.append(new_expense)
    db.session.add(month)

    # db.session.add(new_expense)
    db.session.commit()

    return jsonify({'msg': 'Expense added'}), 201

