import asyncio
from datetime import datetime

from aiohttp import ClientResponse
from sofascore.api.mixins import ClientSessionManagerMixin
from sofascore.api.soccer.categories import SoccerCategoriesApi
from sofascore.api.soccer.schemas.base import Category, UniqueTournament, \
    CategoryList
from sofascore.api.soccer.tournaments import SoccerTournamentApi


class BaseSoccerApi(ClientSessionManagerMixin, SoccerCategoriesApi,
                    SoccerTournamentApi):
    """
    Base API client for interacting with SofaScore's soccer API.
    Provides methods for fetching soccer categories and tournaments.
    """
    BASE_URL = 'https://api.sofascore.com/'




async def main():
    async def get_eng_standings():
        a = BaseSoccerApi()
        c = await a.get_categories()
        category = (await c.find_all_by_name('eng'))[0]
        ut = (await a.get_tournament_by_category(category))[0]
        return await a.get_tournament_standings(ut)
    count=0
    start = datetime.now()
    while True:
        count+=4
        c = await get_eng_standings()
        if not c:
            print(count,datetime.now()-start)
            break
        else:
            print(datetime.now(),count,'ok',count / (datetime.now() - start).total_seconds())
        if count>=1000:
            print(count, datetime.now() - start)
            break
asyncio.run(main())
