from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Union, Optional, Annotated
from contextlib import asynccontextmanager
from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database is cleared")
    await create_tables()
    print("Database is ready")
    yield
    print("Powering off")
    
app = FastAPI(lifespan=lifespan)

    
class Task(BaseModel):
    name: str
    description: Optional[str] = None
   
tasks = []
@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()]
):
    return {"ok":True}
     
# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Write this video")
#     return {
#         "data": task
#     }