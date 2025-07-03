import asyncio
from aiosofascore.client import SofaScoreClient

async def main():
    client = SofaScoreClient(base_url="http://api.sofascore.com/api")
    team_id = 2829
    page = 0
    result = await client.team.last_events.get_last_events(team_id, page)
    print(f"hasNextPage: {result.hasNextPage}")
    for event in result.events:
        tournament_name = event.tournament.name if event.tournament and event.tournament.name else "-"
        print(f"Event id: {event.id}, турнир: {tournament_name}, дата: {event.startTimestamp}")

if __name__ == "__main__":
    asyncio.run(main()) 