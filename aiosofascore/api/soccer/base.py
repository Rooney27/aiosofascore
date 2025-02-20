from aiosofascore.api.mixins import ClientSessionManagerMixin
from aiosofascore.api.soccer.categories import SoccerCategoriesApi
from aiosofascore.api.soccer.event import SoccerEventApi
from aiosofascore.api.soccer.live import SoccerLiveEventsAPI
from aiosofascore.api.soccer.tournaments import SoccerTournamentApi

__all__ =['BaseSoccerApi']

class BaseSoccerApi(ClientSessionManagerMixin, SoccerCategoriesApi,
                    SoccerTournamentApi, SoccerEventApi,SoccerLiveEventsAPI):
    """
    Base API client for interacting with SofaScore's soccer API.
    Provides methods for fetching soccer categories and tournaments.
    """
    BASE_URL = 'https://api.sofascore.com/'
