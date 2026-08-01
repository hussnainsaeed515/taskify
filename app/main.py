from fastapi import FastAPI
from app.routers.task import router as task_router
app =FastAPI(title="Taskify API")
app.include_router(task_router)
@app.get("/")
def root():
    return {"message": "Welcome to Taskify API"}
    






    