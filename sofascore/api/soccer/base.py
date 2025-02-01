from sofascore.api.mixins import ClientSessionManagerMixin
from sofascore.api.soccer.categories import SoccerCategoriesApi
from sofascore.api.soccer.tournaments import SoccerTournamentApi

__all__ =['BaseSoccerApi']

class BaseSoccerApi(ClientSessionManagerMixin, SoccerCategoriesApi,
                    SoccerTournamentApi):
    """
    Base API client for interacting with SofaScore's soccer API.
    Provides methods for fetching soccer categories and tournaments.
    """
    BASE_URL = 'https://api.sofascore.com/'
