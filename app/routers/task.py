from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.tasks import TaskCreate,TaskResponse,TaskUpdate    
from app.database import get_db
from app.models.task import Task
router =APIRouter(prefix="/tasks",tags=["tasks"])

@router.post("/",response_model=TaskResponse)
def create_task(task:TaskCreate,db:Session=Depends(get_db)):
    new_task=Task(title=task.title,description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/",response_model=list[TaskResponse])
def get_all_tasks(db:Session=Depends(get_db)):
    return db.query(Task).all()
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()

    if task.title is not None:
        existing_task.title = task.title
    if task.description is not None:
        existing_task.description = task.description
    if task.is_completed is not None:
        existing_task.is_completed = task.is_completed

    db.commit()
    db.refresh(existing_task)
    return existing_task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(existing_task)
    db.commit()
    return {"message": "Task deleted successfully"}



