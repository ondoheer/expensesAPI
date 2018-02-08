from flask import Blueprint, jsonify, abort, g, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import db
from app.models.user import User
from app.models.category import Category


categories = Blueprint("categories", __name__)


@categories.route("/category", methods=["GET"])
@jwt_required
def query():

    current_user = get_jwt_identity()

    if not current_user:
        return jsonify({'error': 'not authorized'}), 401

    user = User.query.filter_by(email=current_user).first()

    _base_query = db.session.query(Category).filter_by(user_id=user.id).order_by(Category.name)

    categories = _base_query.all()

    return jsonify( Category.serialize_list(categories)), 200


@categories.route("/category", methods=['POST'])
@jwt_required
def create():

    current_user = get_jwt_identity()

    if not current_user:
        return jsonify({'error': 'not authorized'}), 401

    user = User.query.filter_by(email=current_user).first()

    params = request.get_json()
    label = params.get('label', None)

    # This ought to be better validated
    if not label:
        return jsonify({"msg": "Bad request"}), 400

    new_category = Category(
        label=label,
        user_id=user.id
    )

    db.session.add(new_category)
    db.session.commit()

    return jsonify({'msg': 'Category added'}), 201
