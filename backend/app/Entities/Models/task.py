from extensions.alchemy import alchemy as db
from sqlalchemy_serializer import SerializerMixin
from .task_round import TaskRounds


class Task(db.Model, SerializerMixin):
    __tablename__ = "tasks"

    serialize_rules = (
        '-personal.taskscan',
        '-taskaccomplished',
        '-task_round'
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    task_round = db.relationship(TaskRounds, lazy="select", uselist=False)
