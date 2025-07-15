from aiosofascore.api.soccer.services.team.repo import TeamPerformanceRepository
from aiosofascore.api.soccer.services.team.models import TeamPerformanceResponse
from aiosofascore.api.soccer.services.team.common import TeamInfo
from aiosofascore.api.soccer.services.team.repo import TeamInfoRepository
from aiosofascore.api.soccer.services.team.models import TeamLastEventsResponse
from aiosofascore.api.soccer.services.team.repo import TeamLastEventsRepository
from aiosofascore.api.soccer.services.team.repo import TeamPlayersRepository, TeamRankingsRepository, TeamTransfersRepository
from aiosofascore.api.soccer.services.team.models import TeamPlayersResponse, TeamRankingsResponse, TeamTransfersResponse

class TeamPerformanceService:
    """Service for getting team performance."""
    def __init__(self, repository: TeamPerformanceRepository):
        self.repository = repository

    async def get_team_performance(self, team_id: int) -> TeamPerformanceResponse:
        """Get team performance."""
        return await self.repository.get_performance(team_id)

class TeamInfoService:
    """Service for getting team info."""
    def __init__(self, repository: TeamInfoRepository):
        self.repository = repository

    async def get_team_info(self, team_id: int) -> TeamInfo:
        """Get team info."""
        return await self.repository.get_team_info(team_id)

class TeamLastEventsService:
    """Сервис для получения последних событий команды."""
    def __init__(self, repository: TeamLastEventsRepository):
        self.repository = repository

    async def get_last_events(self, team_id: int, page: int = 0) -> TeamLastEventsResponse:
        """Получить последние события команды."""
        return await self.repository.get_last_events(team_id, page=page)

class TeamPlayersService:
    """Service for getting team players."""
    def __init__(self, repository: TeamPlayersRepository):
        self.repository = repository

    async def get_team_players(self, team_id: int) -> TeamPlayersResponse:
        """Get list of team players."""
        return await self.repository.get_team_players(team_id)

class TeamRankingsService:
    """Service for getting team rankings."""
    def __init__(self, repository: TeamRankingsRepository):
        self.repository = repository

    async def get_team_rankings(self, team_id: int) -> TeamRankingsResponse:
        """Get team rankings."""
        return await self.repository.get_team_rankings(team_id)

class TeamTransfersService:
    """Service for getting team transfers."""
    def __init__(self, repository: TeamTransfersRepository):
        self.repository = repository

    async def get_team_transfers(self, team_id: int) -> TeamTransfersResponse:
        """Get team transfers."""
        return await self.repository.get_team_transfers(team_id) 