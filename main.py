from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Union, Optional, Annotated
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import STask, STaskAdd
from router import router as tasks_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database is cleared")
    await create_tables()
    print("Database is ready")
    yield
    print("Powering off")
    
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)  