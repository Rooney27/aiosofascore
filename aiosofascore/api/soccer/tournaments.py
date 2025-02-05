from aiosofascore.api.soccer.schemas.base import UniqueTournament, Category, \
    SeasonList, Standings, UniqueTournamentsList

__all__ = ['SoccerTournamentApi']


class SoccerTournamentApi:
    async def get_tournaments_by_category(self,
                                          category: Category) -> UniqueTournamentsList:
        """
        Fetches a list of unique tournaments for a given soccer category.

        Args:
            category (Category): The soccer category for which to retrieve tournaments.

        Returns:
            list[UniqueTournament]: A list of unique tournaments for the given category.
        """
        async with self:
            content = await self._get(
                f'api/v1/category/{category.id}/unique-tournaments')
            return UniqueTournamentsList(unique_tournaments=content['groups'][0]['uniqueTournaments'])

    async def get_tournament_seasons(self,
                                     unique_tournament: UniqueTournament) -> SeasonList:
        async with self:
            response = await self._get(
                f'api/v1/unique-tournament/{unique_tournament.id}/seasons')
            seasons = response['seasons']
            return SeasonList(seasons=seasons)

    async def get_tournament_standings(self,
                                       unique_tournament: UniqueTournament,
                                       season_year: str = None) -> Standings:
        if season_year:
            season = await (await self.get_tournament_seasons(
                unique_tournament)).get_season_by_year(season_year)
        else:
            season = await (await self.get_tournament_seasons(
                unique_tournament)).get_current_season()

        async with self:
            response = await self._get(
                f'api/v1/unique-tournament/{unique_tournament.id}/season/{season.id}/standings/home')
            standings = response['standings'][0]
            return Standings(**standings)
