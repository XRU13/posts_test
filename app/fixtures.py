import asyncio

from sqlalchemy.ext.asyncio import async_session

from app.adapters.database.models.post import Post
from app.api.settings import get_db_session

MOCK_DATA = [
    {"category": "tech", "content": "Python is awesome. Async programming is powerful. Python is great!"},
    {"category": "tech", "content": "FastAPI is a modern web framework for building APIs with Python."},
    {"category": "news", "content": "Breaking news in technology: Python overtakes JavaScript in popularity."},
    {"category": "news", "content": "Global events today include economic changes and tech advancements."},
    {"category": "health", "content": "Health experts suggest regular exercise and a healthy diet."},
    {"category": "health", "content": "Mental health is just as important as physical health."},
]


async def load_fixtures():
    async with get_db_session() as session:
        async with session.begin():
            posts = [Post(**item) for item in MOCK_DATA]
            session.add_all(posts)


if __name__ == "__main__":
    asyncio.run(load_fixtures())
