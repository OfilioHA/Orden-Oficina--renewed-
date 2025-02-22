from flask import Blueprint, jsonify, request
from extensions.guard import guard
import flask_praetorian

auth_bp = Blueprint('authentication', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    req = request.get_json(force=True)
    username = req.get("username", None)
    password = req.get("password", None)
    user = guard.authenticate(username, password)
    ret = {"token": guard.encode_jwt_token(user)}
    return (jsonify(ret), 200)


@auth_bp.route('/logout', methods=['POST'])
@flask_praetorian.auth_required
def logout():
    # Check if Flask Praetorian needs to delete the token
    return ('', 204)


@auth_bp.route('/alive', methods=['GET'])
@flask_praetorian.auth_required
def alive():
    return ('', 204)
