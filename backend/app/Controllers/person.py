from flask import Blueprint, jsonify
from app.Entities import Personal

person_bp = Blueprint('person', __name__, url_prefix='/person');

@person_bp.route('/')
def index():
    persons = Personal.query.all()
    persons = [person.to_dict() for person in persons]
    return jsonify(persons)

