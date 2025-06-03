from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncResult

@dataclass
class PostQueryResult:
    total: int
    result: AsyncResult
