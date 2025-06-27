from pprint import pprint
from typing import Literal

from aiosofascore.adapters.http_client import HttpSessionManager
from aiosofascore.api.soccer.services.search.models import SearchEntityResult


class SearchResult:
    def __init__(self,query: str, http: "HttpSessionManager"):
        self.query = query
        self.page = -1
        self.http = http

    async def get_next_page(self) -> list["SearchEntityResult"]:
        self.page += 1
        params = {
            'q': self.query,
            'page': self.page,
        }
        async with self.http:
            resp = await self.http.get('/v1/search/all', params=params)
            return [SearchEntityResult(**e) for e in resp['results']]

class SearchRepository:
    def __init__(self, http: "HttpSessionManager"):
        self.http = http

    async def search(self, query: str,type:Literal["team", "player", "event"]|None=None):
        result = SearchResult(query, self.http)
        while True:
            items = await result.get_next_page()
            if not items:
                break
            for item in items:
                if not type:
                    yield item
                else:
                    if item.type == type:
                        yield item
