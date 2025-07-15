from aiosofascore.adapters.http_client import HttpSessionManager
from aiosofascore.api.soccer.services.team import (
    TeamPerformanceService, TeamPerformanceRepository,
    TeamInfoService, TeamInfoRepository,
    TeamLastEventsService, TeamLastEventsRepository,
    TeamPlayersService, TeamPlayersRepository,
    TeamRankingsService, TeamRankingsRepository,
    TeamTransfersService, TeamTransfersRepository
)
from aiosofascore.api.soccer.services.search import SearchService, SearchRepository

class SofaScoreTeamServices:
    """Groups all team-related services."""
    def __init__(self, http: HttpSessionManager):
        self.performance: TeamPerformanceService = TeamPerformanceService(TeamPerformanceRepository(http))
        self.info: TeamInfoService = TeamInfoService(TeamInfoRepository(http))
        self.last_events: TeamLastEventsService = TeamLastEventsService(TeamLastEventsRepository(http))
        self.players: TeamPlayersService = TeamPlayersService(TeamPlayersRepository(http))
        self.rankings: TeamRankingsService = TeamRankingsService(TeamRankingsRepository(http))
        self.transfers: TeamTransfersService = TeamTransfersService(TeamTransfersRepository(http))

class SofaScoreSearchServices:
    """Groups search services."""
    def __init__(self, http: HttpSessionManager):
        self.search: SearchService = SearchService(SearchRepository(http))

class SofaScoreClient:
    """
    Main facade for working with the SofaScore API.
    Example:
        client = SofaScoreClient(base_url="http://api.sofascore.com")
        players = await client.team.players.get_team_players(team_id)
    """
    def __init__(self, base_url: str):
        self.http: HttpSessionManager = HttpSessionManager(base_url=base_url)
        self.team: SofaScoreTeamServices = SofaScoreTeamServices(self.http)
        self.search: SofaScoreSearchServices = SofaScoreSearchServices(self.http)

class BaseClient:
    pass