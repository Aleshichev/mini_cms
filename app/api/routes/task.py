import uuid
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import ALL
from app.core.database import get_db
from app.crud.auth import require_role
from app.crud.task import create_task, delete_task, get_task, get_tasks
from app.schemas.task import TaskCreate, TaskRead
from app.utils.exceptions import get_or_404

# from app.tasks.notify import notify_about_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskRead)
async def create_new_task(
    task_in: TaskCreate,
    session: AsyncSession = Depends(get_db),
    user=Depends(require_role(ALL)),
):
    new_task = await create_task(session, task_in)
    # notify_about_task.delay(str(new_task.id))
    return new_task


@router.get("/", response_model=list[TaskRead])
async def read_tasks(
    project_id: uuid.UUID | None = None,
    manager_id: uuid.UUID | None = None,
    is_completed: bool | None = None,
    search: str | None = None,
    due_date_to: datetime | None = None,
    session: AsyncSession = Depends(get_db),
    user=Depends(require_role(ALL)),
):
    tasks = get_or_404(
        await get_tasks(
            session, project_id, manager_id, is_completed, search, due_date_to
        ),
        "Tasks not found",
    )
    return tasks


@router.get("/{task_id}", response_model=TaskRead)
async def read_task(
    task_id: uuid.UUID,
    session: AsyncSession = Depends(get_db),
    user=Depends(require_role(ALL)),
):
    task = get_or_404(await get_task(session, task_id), "Task not found")
    return task


@router.delete("/{task_id}", status_code=200)
async def delete_task_by_id(
    task_id: uuid.UUID,
    session: AsyncSession = Depends(get_db),
    user=Depends(require_role(ALL)),
):
    get_or_404(await delete_task(session, task_id), "Task not found")
    return {"message": "Task deleted"}
