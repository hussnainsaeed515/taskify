from fastapi import FastAPI
from app.database import engine, Base
import app.models.task
import app.models.user
from app.routers.task import router as task_router
from app.routers.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Taskify API")

app.include_router(task_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Welcome to Taskify API"}

    