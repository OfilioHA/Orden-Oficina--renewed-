from flask import Blueprint

person_bp = Blueprint('person', __name__, url_prefix='/person');

@person_bp.route('/')
def index():
    return 'Person URL';

