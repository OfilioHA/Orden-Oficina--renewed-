from extensions.alchemy import alchemy as db
from sqlalchemy_serializer import SerializerMixin
from app.Entities.Mixins import UserMixin, DateMixin

class TaskAccomplished(db.Model, SerializerMixin, UserMixin, DateMixin):

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    task_round_id = db.Column(db.Integer, db.ForeignKey('task_rounds.id'), nullable=False)
    personal_id = db.Column(db.Integer, db.ForeignKey('personal.id'), nullable=False)
    accomplished_at = db.Column(db.String, nullable=False)

    serialize_rules = (
        '-personal.taskaccomplished',
    )

    def __init__(self, task_id, task_round_id, personal_id, accomplished_at):
        UserMixin.__init__(self)
        DateMixin.__init__(self)
        self.task_id = task_id
        self.task_round_id = task_round_id;
        self.personal_id  = personal_id;
        self.accomplished_at = accomplished_at

    personal = db.relationship(
        "Personal", 
        backref=db.backref(
            "taskaccomplished", 
            lazy="dynamic"
        )
    )

