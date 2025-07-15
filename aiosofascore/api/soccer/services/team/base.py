from aiosofascore.adapters.http_client import HttpSessionManager
from aiosofascore.exception import ResponseParseContentError

class BaseRepository:
    def __init__(self, http: "HttpSessionManager"):
        self.http = http

    async def _get(self, url: str, model_cls, params: dict = None):
        async with self.http:
            try:
                resp = await self.http.get(url, params=params)
                data = resp if isinstance(resp, dict) else await resp.json()
                return model_cls(**data)
            except ResponseParseContentError as e:
                print(await e.async_str())
                raise 