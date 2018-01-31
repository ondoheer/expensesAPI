from flask import Blueprint, jsonify, request

from flask_jwt_simple import create_jwt


auth = Blueprint("auth", __name__)


@auth.route('/login', methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSOn in Request"}), 400

    params = request.get_json()
    username = params.get('username', None)
    email = params.get('email', None)
    password = params.get('password', None)

    if not username:
        if not email:
            return jsonify({"msg": "Username or email Missing"}), 400

    if not password:
        return jsonify({"msg": "Missing password"})

    # validate user logic

    ret = {"token": create_jwt(identity=username)}
    return jsonify(ret), 200
