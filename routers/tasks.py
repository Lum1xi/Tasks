from fastapi import APIRouter, Response, HTTPException, Depends
from fastapi.responses import JSONResponse
from services.task_service import get_all_tasks, create_task, update_task, delete_task
from schemas.task import CreateTask, UpdateTask, DeleteTask, Task

tasks = APIRouter()

@tasks.get("/tasks")
def get_tasks():
    return get_all_tasks()

@tasks.post("/create_task")
def add_create_task(data: CreateTask):
    result = create_task(data)
    if result and type(result) is dict:
        return JSONResponse(content=result, status_code=201)
    else:
        raise HTTPException(status_code=400, detail="Failed to create task")

@tasks.put("/update_task/{task_id}")
def update_task_by_id(task_id: int, data: UpdateTask):
    result = update_task(task_id, data)
    if result:
        return JSONResponse(content=result, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@tasks.delete("/delete_task/{task_id}")
def delete_task_by_id(task_id: int):
    result = delete_task(task_id)
    if result:
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=404, detail="Task not found")