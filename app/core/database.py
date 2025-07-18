from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
)
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from app.core.config import settings

engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URL, echo=False, future=True
)

async_session = async_sessionmaker(
    engine, expire_on_commit=False, autoflush=False, autocommit=False
)


async def dispose():
    await engine.dispose()


async def get_db():
    async with async_session() as session:
        yield session

@asynccontextmanager
async def get_db_context():
    async with async_session() as session:
        yield session