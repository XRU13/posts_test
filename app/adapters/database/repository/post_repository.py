from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.adapters.database.models.post import Post
from app.apllication.dataclasses.dataclass import PostQueryResult


class PostRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_posts_with_total(
        self,
        category: Optional[str],
        keywords: Optional[List[str]],
        limit: int,
        offset: int,
    ) -> PostQueryResult:
        query = select(Post)

        if category:
            query = query.where(Post.category == category)

        if keywords:
            for kw in keywords:
                query = query.where(Post.content.ilike(f"%{kw}%"))

        # Общий счётчик
        total_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(total_query)

        # Стриминг результатов
        stream = await self.session.stream(query.offset(offset).limit(limit))
        return PostQueryResult(
            total=total,
            result=stream,
        )