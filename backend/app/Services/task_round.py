from app.Entities import TaskRoundRepository
# from app.Exceptions import TaskRoundFullTasks

MAX_AMOUNT = 3


class TaskRoundService():

    @staticmethod
    def last_round(id):
        active_round = TaskRoundRepository.task_active_round(id)
        if (active_round is None):
            raise Exception('No Active round')
        return active_round

    @staticmethod
    def validate_tasks_amount(actual_round, person):
        tasks_accomplished = TaskRoundRepository.person_tasks_active_round(
            actual_round,
            person
        )
        tasks_accomplished_amount = tasks_accomplished.count()
        if (tasks_accomplished_amount >= MAX_AMOUNT):
            raise Exception("Ronda cumplida")
