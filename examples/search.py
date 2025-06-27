import asyncio
from datetime import datetime

from aiosofascore.adapters.http_client import HttpSessionManager
from aiosofascore.api.soccer.services.search.repo import SearchRepository
from aiosofascore.api.soccer.services.search.service import SearchService


async def main():
    s = SearchService(repository=SearchRepository(http=HttpSessionManager('http://api.sofascore.com/api')))
    # Search managers with name Alexander
    async for result in s.search_entities("Alexander", type="manager"):
        print(result.entity.name)
        print(result.type)
        print(result.entity.team.name)
        print('===================')
    # Search matches Arsenal vs Manchester united
    async for result in s.search_entities("Arsenal vs Manchester united", type="event"):
        print(result.entity.name)
        print(result.entity.startTimestamp)
        if result.entity.status.type=="finished":
            print(result.entity.homeScore.display,'-', result.entity.awayScore.display)
        print('===================')


asyncio.run(main())