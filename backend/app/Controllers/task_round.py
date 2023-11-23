from flask import Blueprint, jsonify
from app.Services import PersonalService
from app.Services import TaskService
from app.Services import TaskAccomplishedService

round_bp = Blueprint('round', __name__, url_prefix='/round')

@round_bp.route("/<int:id>/personal")
def round_personal(id):
    task = TaskService.from_round(id)
    task_round = task.task_round
    personal = PersonalService.from_task(task.id)
    personal = TaskAccomplishedService.from_personal(personal, task_round)
    return jsonify(personal)
