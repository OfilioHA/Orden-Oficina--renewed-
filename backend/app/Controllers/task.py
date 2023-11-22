from flask import Blueprint, jsonify
from app.Services import TaskAccomplishedService
from app.Services import TaskRoundService
from app.Services import PersonalService
from app.Entities import Task

task_bp = Blueprint('task', __name__, url_prefix='/task')


@task_bp.route('/')
def index():
    tasks = Task.query.all()
    tasks = [task.to_dict() for task in tasks]
    return jsonify(tasks)


@task_bp.route("/<int:id>/personal")
def personal_task(id):
    active_round = TaskRoundService.last_round(id)
    personal = PersonalService.from_task(id)
    personal = TaskAccomplishedService.from_personal(personal, active_round)
    return jsonify({
        "list": personal,
        "round": active_round.number
    })
