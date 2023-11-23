from app.Entities import TaskAccomplished
from app.Entities import TaskRounds
from app.Entities import Personal
from app.Entities import Task


class TaskAccomplishedRepository():
    @staticmethod
    def from_person(personal, active_round):
        return TaskAccomplished.query\
            .join(Task, TaskAccomplished.task_id == Task.id)\
            .join(TaskRounds, TaskAccomplished.task_round_id == TaskRounds.id)\
            .join(Personal, TaskAccomplished.personal_id == Personal.id)\
            .filter(
                Personal.id == personal.id,
                TaskRounds.id == active_round.id
            )
    
    @staticmethod
    def from_round(round_id):
        return TaskAccomplished.query\
            .join(Task, TaskAccomplished.task_id == Task.id)\
            .join(TaskRounds, TaskAccomplished.task_round_id == TaskRounds.id)\
            .join(Personal, TaskAccomplished.personal_id == Personal.id)\
            .filter(
                TaskRounds.id == round_id
            )
