from typing import AsyncGenerator, Literal

from aiosofascore.api.soccer.services.search.models import SearchEntityResult
from aiosofascore.api.soccer.services.search.repo import SearchRepository


class SearchService:
    def __init__(self, repository: SearchRepository):
        self.repository = repository

    async def search_entities(
        self,
        query: str,
        type: Literal["team", "player", "event", "manager"] | None = None
    ) -> AsyncGenerator[SearchEntityResult, None]:
        async for item in self.repository.search(query, type=type):
            yield item