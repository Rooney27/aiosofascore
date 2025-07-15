"""
Example usage of SofaScoreClient for working with team endpoints:
- Players
- Last events
- Performance
- Rankings
- Transfers
"""
import asyncio
from aiosofascore.client import SofaScoreClient

TEAM_ID = 2819
PAGE = 0

async def show_players(client, team_id):
    print("\n=== Team players ===")
    result = await client.team.players.get_team_players(team_id)
    if result.players:
        print(f"Total players: {len(result.players)}")
        for i, player_item in enumerate(result.players, 1):
            player = player_item.player
            print(f"{i:2d}. {player.name} | {player.position or '-'} | #{player.jerseyNumber or '-'}")
    else:
        print("No players found")

async def show_last_events(client, team_id, page=0):
    print("\n=== Last events ===")
    result = await client.team.last_events.get_last_events(team_id, page)
    print(f"hasNextPage: {result.hasNextPage}")
    for event in result.events:
        tournament_name = event.tournament.name if event.tournament and event.tournament.name else "-"
        print(f"Event id: {event.id}, tournament: {tournament_name}, date: {event.startTimestamp}")

async def show_performance(client, team_id):
    print("\n=== Team performance ===")
    result = await client.team.performance.get_team_performance(team_id)
    if result.events:
        print(f"Total matches: {len(result.events)}")
        for i, event in enumerate(result.events[:5], 1):
            home = event.homeTeam.name if event.homeTeam else '-'
            away = event.awayTeam.name if event.awayTeam else '-'
            print(f"{i:2d}. {home} vs {away}")
            if event.homeScore and event.awayScore:
                print(f"     Score: {event.homeScore.current or 0} - {event.awayScore.current or 0}")
            if event.tournament:
                print(f"     Tournament: {event.tournament.name}")
    else:
        print("No matches found")
    if result.points:
        print("Points by position:")
        for pos, pts in result.points.items():
            print(f"  {pos}: {pts}")

async def show_rankings(client, team_id):
    print("\n=== Team rankings ===")
    result = await client.team.rankings.get_team_rankings(team_id)
    if result.rankings:
        for r in result.rankings:
            print(f"{r.rowName or '-'}: {r.ranking} place, {r.points} points, tournament: {r.currentTournamentName}")
    else:
        print("No ranking data")

async def show_transfers(client, team_id):
    print("\n=== Incoming transfers ===")
    result = await client.team.transfers.get_team_transfers(team_id)
    if result.transfersIn:
        for t in result.transfersIn:
            print(f"{t.player.name if t.player else '-'} from {t.fromTeamName or '-'} for {t.transferFeeDescription or '-'}")
    else:
        print("No incoming transfers")
    print("\n=== Outgoing transfers ===")
    if result.transfersOut:
        for t in result.transfersOut:
            print(f"{t.player.name if t.player else '-'} to {t.toTeamName or '-'} for {t.transferFeeDescription or '-'}")
    else:
        print("No outgoing transfers")

async def main():
    client = SofaScoreClient("http://api.sofascore.com")
    await show_players(client, TEAM_ID)
    await show_last_events(client, TEAM_ID, PAGE)
    await show_performance(client, TEAM_ID)
    await show_rankings(client, TEAM_ID)
    await show_transfers(client, TEAM_ID)

if __name__ == "__main__":
    asyncio.run(main()) 