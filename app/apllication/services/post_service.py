import re
from collections import Counter
from typing import Optional, List

from app.adapters.database.models.post import Post
from app.api.schema import PostAnalysis
from app.apllication.interfaces.post_interface import IPostRepo


class PostService:
	post_repo: IPostRepo

	def __init__(self, post_repo):
		self.post_repo = post_repo

	async def get_post(
		self,
		category: Optional[str],
		keywords: Optional[List[str]],
		limit: int,
		offset: int,
	):
		query_result = await self.post_repo.get_posts_with_total(
			category=category,
			keywords=keywords,
			limit=limit,
			offset=offset
		)

		items = []
		async for row in query_result.result:
			post: Post = row[0]
			items.append(self._analyze_content(post))

		return {
			"total": query_result.total,
			"items": items,
			"limit": limit,
			"offset": offset
		}

	def _analyze_content(self, post: Post) -> PostAnalysis:
		words = re.findall(r'\w+', post.content.lower())
		freq = Counter(words)
		tags = [word for word, count in freq.items() if count > 2]

		return PostAnalysis(
			id=post.id,
			category=post.category,
			top_words=freq.most_common(5),
			tags=tags,
		)
