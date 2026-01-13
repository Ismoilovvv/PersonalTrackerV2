from utils.file_handler import load_data, save_data
from tasks.task import Task

TASK_FILE = 'data/tasks.json'

class TaskManager:
    def add_task(self, title):
        task = Task(title)
        tasks = load_data(TASK_FILE)
        tasks.append(task.to_dict())
        save_data(TASK_FILE, tasks)

    def delete_task(self, index):
        tasks = load_data(TASK_FILE)
        del tasks[index]
        save_data(TASK_FILE, tasks)

    def get_all_tasks(self):
        return load_data(TASK_FILE)

    def get_pending_tasks(self):
        tasks = load_data(TASK_FILE)
        return [task for task in tasks if not task['completed']]

    def mark_task_completed(self, index):
        tasks = load_data(TASK_FILE)
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            save_data(TASK_FILE, tasks)

    def get_task_summary(self):
        tasks = load_data(TASK_FILE)
        total = len(tasks)
        completed = sum(1 for task in tasks if task['completed'])
        return total, completed