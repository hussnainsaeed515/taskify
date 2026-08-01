from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.tasks import TaskCreate,TaskResponse
from app.database import get_db
from app.models.task import Task
router =APIRouter(prefix="/tasks",tags=["tasks"])

@router.post("/",response_model=TaskResponse)
async def create_task(task:TaskCreate,db:Session=Depends(get_db)):
    new_task=Task(title=task.title,description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/",response_model=list[TaskResponse])
async def get_all_tasks(db:Session=Depends(get_db)):
    return db.query(Task).all()
    
