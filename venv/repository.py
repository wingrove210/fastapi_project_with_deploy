from database import new_session, TaskORM
from main import STaskAdd
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskORM(**task_dict)
            session.add(task)
            await session.commit()
            return task.id
            
    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models