from aiosofascore.adapters.http_client import HttpSessionManager


__all__ =['BaseSoccerApi']

class BaseSoccerApi(HttpSessionManager):
    """
    Base API client for interacting with SofaScore's soccer API.
    Provides methods for fetching soccer categories and tournaments.
    """
    BASE_URL = 'https://api.sofascore.com/'
