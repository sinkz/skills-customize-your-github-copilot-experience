from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

tasks = []

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return tasks

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, completed: bool):
    for task in tasks:
        if task.id == task_id:
            task.completed = completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
