from flask import Blueprint, jsonify, request

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity
)
from app.validators import validate_email, validate_fullname, validate_password
from app.models.user import User
from app.models import db
from app.extensions import bcrypt

auth = Blueprint("auth", __name__)


@auth.route('/login', methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in Request"}), 400

    params = request.get_json()
    print(params)
    email = params.get('email', None)
    password = params.get('password', None)

    if not email:
        return jsonify({"msg": "Email Missing"}), 400

    if not password:
        return jsonify({"msg": "Missing password"})

    # validate user logic
    # the identity is the one that will be returned by get_jwt_identity

    should_login = User.validate_password(email, password)

    if not should_login:
        return jsonify({'msg': 'invalid email or password'}), 400

    token = {
        "access_token": create_access_token(identity=email),
        "refresh_token": create_refresh_token(identity=email)
    }
    return jsonify(token), 200


@auth.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200



@auth.route('/register', methods=["POST"])
def register():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in Request"}), 400

    params = request.get_json()
    email = params.get('email', None)
    password = params.get('password', None)
    fullname = params.get('fullname', None)

    # validate fields
    if not email:
        return jsonify({"msg": "Email Missing"}), 400
    is_email_valid, error = validate_email(email)
    if not is_email_valid:
        return jsonify({"msg": "that is not a valid email", "err": error}), 400
    user_exists = db.session.query(User).filter_by(email=email).first()
    if user_exists:
        return jsonify({'msg': 'user with those unique attributes already exists'}), 500

    if not fullname:
        return jsonify({"msg": "Full name required"}), 400
    is_fullname_valid, error = validate_fullname(fullname)
    if not is_fullname_valid:
        return jsonify({"msg": "that is not a valid fullname", "err": error}), 400

    if not password:
        return jsonify({"msg":"Password required"}), 400
    is_password_valid, error = validate_password(password)
    if not is_password_valid:
        return jsonify({"msg": "that is not a valid password", "err": error}), 400


    # now we process the registration

    new_user = User(
        fullname=fullname,
        email=email,
        password=password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'msg': 'User created'}), 201


