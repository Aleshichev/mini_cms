# app/schemas/project.py
import uuid
from datetime import datetime

from pydantic import BaseModel

from app.models.project import ProjectsName
from app.schemas.user import UserBase


class ProjectBase(BaseModel):
    name: ProjectsName = ProjectsName.web_site
    description: str | None = None

    class Config:
        from_attributes = True


class ProjectCreate(ProjectBase):
    users: list[uuid.UUID] = []


class ProjectUpdate(ProjectBase):
    name: str | None = None
    description: str | None = None
    users: list[uuid.UUID] | None = None


class ProjectRead(ProjectCreate):
    id: uuid.UUID
    created_at: datetime
    users: list[UserBase] = []
