from typing import Any

from schemas.task import CreateTask, DeleteTask, UpdateTask, Task

tasks = {}

def get_all_tasks() -> dict[Any, Any]:
    return tasks

def create_task(task_data: CreateTask) -> Task:
    task_id = len(tasks) + 1
    tasks[task_id] = Task(id=task_id, title=task_data.title, description=task_data.description, state=task_data.state).model_dump()
    return tasks[task_id]

def update_task(task_id: UpdateTask, task_data):
    if task_id not in tasks:
        return None
    task = tasks[task_id]
    if task_data.title is not None:
        task['title'] = task_data.title
    if task_data.description is not None:
        task['description'] = task_data.description
    if task_data.state is not None:
        task['state'] = task_data.state
    return task

def delete_task(task_id: DeleteTask):
    return tasks.pop(task_id, None)