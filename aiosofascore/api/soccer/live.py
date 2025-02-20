from aiosofascore.api.soccer.schemas import EventLiveResults


class SoccerLiveEventsAPI:
    async def get_live_events(self)->EventLiveResults:
        async with self:
            content = await self._get('api/v1/sport/football/events/live')
            return EventLiveResults(**content)