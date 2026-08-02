from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate    
from app.database import get_db
from app.models.task import Task
router = APIRouter(prefix="/tasks", tags=["tasks"])
from app.core.security import get_current_user


@router.post("", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    new_task = Task(title=task.title, description=task.description)
    try:
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred while creating task")

@router.get("", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.title is not None:
        existing_task.title = task.title
    if task.description is not None:
        existing_task.description = task.description
    if task.is_completed is not None:
        existing_task.is_completed = task.is_completed

    try:
        db.commit()
        db.refresh(existing_task)
        return existing_task
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred while updating task")


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    try:
        db.delete(existing_task)
        db.commit()
        return {"message": "Task deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred while deleting task")
    



