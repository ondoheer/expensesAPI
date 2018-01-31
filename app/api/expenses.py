from flask import Blueprint, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

expenses = Blueprint("expenses", __name__)

@expenses.route("/expense", methods=["GET"])
@jwt_required
def all():


    return jsonify({'hello from': get_jwt_identity()}), 200
