from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.adapters.database.repository.post_repository import PostRepo
from app.apllication.services.post_service import PostService

DATABASE_URL = 'postgresql+asyncpg://postgres:postgres@db:5432/posts_db'

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSession = async_sessionmaker(engine, expire_on_commit=False)

@asynccontextmanager
async def get_db_session() -> AsyncGenerator:
	async with AsyncSession() as session:
		yield session
		await session.commit()


def create_post_repo(
	session: AsyncSession = Depends(get_db_session)
) -> PostRepo:
	return PostRepo(session=session)


def create_posts_services(
	post_repo: PostRepo = Depends(create_post_repo),
) -> PostService:
	return PostService(post_repo=post_repo)