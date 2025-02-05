from aiosofascore.api.soccer.schemas.base import PregameTeamForm, H2H, \
    EventManagers


class SoccerEventApi:

    async def get_pregame_form(self,event_id:str)->PregameTeamForm:
        async with self:
            result = self._get(f'api/v1/event/{event_id}/pregame-form')
            return PregameTeamForm(**result)

    async def get_h2h(self,event_id:str)->H2H:
        async with self:
            result = self._get(f'api/v1/event/{event_id}/h2h')
            return H2H(**result)

    async def get_managers(self,event_id:str)->EventManagers:
        async with self:
            result = self._get(f'api/v1/event/{event_id}/managers')
            return EventManagers(**result)