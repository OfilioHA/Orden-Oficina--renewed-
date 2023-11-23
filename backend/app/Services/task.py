from app.Entities import TaskRepository

class TaskService():

    @staticmethod
    def from_round(round_id):
        task = TaskRepository.from_round(round_id)
        return task.one();