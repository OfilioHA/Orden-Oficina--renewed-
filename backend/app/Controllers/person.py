from flask import Blueprint, jsonify, request
from app.Services import PersonalService
from app.Entities import Personal


person_bp = Blueprint('person', __name__, url_prefix='/person')


@person_bp.route('/')
def index():
    persons = Personal.query.all()
    persons = [person.to_dict() for person in persons]
    return jsonify(persons)


@person_bp.route("/personal", methods=['POST'])
def create():
    req = request.get_json(force=True)
    personal = PersonalService.create(
        req['firstnames'],
        req['lastnames'],
        req['birthday'],
        req['gender_id'],
        req['type_id'],
    )
    return jsonify(personal.id)
