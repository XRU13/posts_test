from abc import ABC, abstractmethod
from typing import Optional, List

from app.apllication.dataclasses.dataclass import PostQueryResult


class IPostRepo(ABC):

	@abstractmethod
	async def get_posts_with_total(
		self,
		category: Optional[str],
		keywords: Optional[List[str]],
		limit: int,
		offset: int,
	) -> PostQueryResult:
		pass
