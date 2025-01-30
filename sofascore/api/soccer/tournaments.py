from sofascore.api.soccer.schemas.base import UniqueTournament, Category, \
    SeasonList, Standings

__all__ = ['SoccerTournamentApi']


class SoccerTournamentApi:
    async def get_tournament_by_category(self, category: Category) -> list[
        UniqueTournament]:
        """
        Fetches a list of unique tournaments for a given soccer category.

        Args:
            category (Category): The soccer category for which to retrieve tournaments.

        Returns:
            list[UniqueTournament]: A list of unique tournaments for the given category.
        """
        async with self:
            response = await self._get(
                f'api/v1/category/{category.id}/unique-tournaments')
            try:
                content = await response.json()
            except Exception as e:
                print(response.request_info)
                print(response.status)
                print(response.content)
            return [
                UniqueTournament(**uniqueTournament)
                for uniqueTournament in
                content['groups'][0]['uniqueTournaments']
            ]

    async def get_tournament_seasons(self,
                                     unique_tournament: UniqueTournament) -> SeasonList:
        async with self:
            response = await self._get(
                f'api/v1/unique-tournament/{unique_tournament.id}/seasons')
            seasons = (await response.json())['seasons']
            return SeasonList(seasons=seasons)

    async def get_tournament_standings(self,
                                       unique_tournament: UniqueTournament,
                                       season_year: str = None):
        if season_year:
            season = await (await self.get_tournament_seasons(unique_tournament)).get_season_by_year(season_year)
        else:
            season = await (await self.get_tournament_seasons(unique_tournament)).get_current_season()

        async with self:
            response = await self._get(
                f'api/v1/unique-tournament/{unique_tournament.id}/season/{season.id}/standings/home')
            standings = (await response.json())['standings'][0]
            print(standings)
            return Standings(**standings)
