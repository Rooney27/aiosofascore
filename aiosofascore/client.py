from aiosofascore.adapters.http_client import HttpSessionManager
from aiosofascore.api.soccer.services.team import (
    TeamPerformanceService, TeamPerformanceRepository,
    TeamInfoService, TeamInfoRepository,
    TeamLastEventsService, TeamLastEventsRepository
)
from aiosofascore.api.soccer.services.search import SearchService, SearchRepository

class SofaScoreTeamServices:
    def __init__(self, http: HttpSessionManager):
        self.performance = TeamPerformanceService(TeamPerformanceRepository(http))
        self.info = TeamInfoService(TeamInfoRepository(http))
        self.last_events = TeamLastEventsService(TeamLastEventsRepository(http))

class SofaScoreSearchServices:
    def __init__(self, http: HttpSessionManager):
        self.search = SearchService(SearchRepository(http))

class SofaScoreClient:
    def __init__(self, base_url: str):
        self.http = HttpSessionManager(base_url=base_url)
        self.team = SofaScoreTeamServices(self.http)
        self.search = SofaScoreSearchServices(self.http)

class BaseClient:
    pass