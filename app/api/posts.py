from fastapi import APIRouter, Depends, Query
from typing import List, Optional

from app.api.schema import PostAnalysis
from app.api.settings import create_posts_services
from app.apllication.services.post_service import PostService

router = APIRouter()

@router.get('/posts', response_model=List[PostAnalysis])
async def get_posts(
    category: Optional[str] = None,
    keywords: Optional[List[str]] = Query(default=None),
    limit: int = 10,
    offset: int = 0,
    post_service: PostService = Depends(create_posts_services)
) -> List[PostAnalysis]:
    return await post_service.get_post(
        category=category,
        keywords=keywords,
        limit=limit,
        offset=offset,
    )
