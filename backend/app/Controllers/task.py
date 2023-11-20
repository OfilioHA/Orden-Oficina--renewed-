from flask import Blueprint, jsonify
from app.Entities import Task

task_bp = Blueprint('task', __name__, url_prefix='/task');

@task_bp.route('/')
def index():
    tasks = Task.query.all()
    tasks = [task.to_dict() for task in tasks]
    return jsonify(tasks)