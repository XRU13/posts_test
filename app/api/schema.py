from pydantic.v1 import BaseModel
from typing import List, Tuple

class PostAnalysis(BaseModel):
    id: int
    category: str
    top_words: List[Tuple[str, int]]
    tags: List[str]
