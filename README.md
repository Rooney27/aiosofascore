[🇷🇺 Русский](README.md) | [🇬🇧 English](README.en.md)

![PyPI Version](https://img.shields.io/pypi/v/aiosofascore)
[![PyPI Downloads](https://static.pepy.tech/badge/aiosofascore)](https://pepy.tech/projects/aiosofascore)
![LICENSE](https://img.shields.io/badge/License-MIT-blue.svg)

# Aiosofascore

**Aiosofascore** — асинхронный Python-клиент для SofaScore API (футбол), предоставляющий удобный доступ к данным о командах, матчах, поиску и статистике.

## Возможности

- Получение информации о командах, последних матчах, статистике
- Поиск игроков, команд, событий, менеджеров
- Асинхронный HTTP-клиент на базе aiohttp

## Установка

```bash
pip install aiosofascore
```

### Пример работы с командой (все основные возможности)
```python
import asyncio
from aiosofascore.client import SofaScoreClient

TEAM_ID = 2819  # Можно заменить на нужный ID
PAGE = 0

async def main():
    client = SofaScoreClient("http://api.sofascore.com")
    # Игроки
    players = await client.team.players.get_team_players(TEAM_ID)
    print(f"\n=== Игроки команды ===")
    if players.players:
        for i, player_item in enumerate(players.players, 1):
            player = player_item.player
            print(f"{i:2d}. {player.name} | {player.position or '-'} | №{player.jerseyNumber or '-'}")
    # Последние события
    last_events = await client.team.last_events.get_last_events(TEAM_ID, PAGE)
    print(f"\n=== Последние события ===")
    for event in last_events.events:
        tournament_name = event.tournament.name if event.tournament and event.tournament.name else "-"
        print(f"Event id: {event.id}, турнир: {tournament_name}, дата: {event.startTimestamp}")
    # Производительность
    perf = await client.team.performance.get_team_performance(TEAM_ID)
    print(f"\n=== Производительность ===")
    if perf.events:
        for i, event in enumerate(perf.events[:5], 1):
            home = event.homeTeam.name if event.homeTeam else '-'
            away = event.awayTeam.name if event.awayTeam else '-'
            print(f"{i:2d}. {home} vs {away}")
            if event.homeScore and event.awayScore:
                print(f"     Счёт: {event.homeScore.current or 0} - {event.awayScore.current or 0}")
    # Рейтинги
    rankings = await client.team.rankings.get_team_rankings(TEAM_ID)
    print(f"\n=== Рейтинги ===")
    if rankings.rankings:
        for r in rankings.rankings:
            print(f"{r.rowName or '-'}: {r.ranking} место, {r.points} очков, турнир: {r.currentTournamentName}")
    # Трансферы
    transfers = await client.team.transfers.get_team_transfers(TEAM_ID)
    print(f"\n=== Входящие трансферы ===")
    if transfers.transfersIn:
        for t in transfers.transfersIn:
            print(f"{t.player.name if t.player else '-'} из {t.fromTeamName or '-'} за {t.transferFeeDescription or '-'}")
    print(f"\n=== Исходящие трансферы ===")
    if transfers.transfersOut:
        for t in transfers.transfersOut:
            print(f"{t.player.name if t.player else '-'} в {t.toTeamName or '-'} за {t.transferFeeDescription or '-'}")

if __name__ == "__main__":
    asyncio.run(main())
```

## License
This project is licensed under the MIT License — see the LICENSE file for details.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact me via vasilewskij.fil@gmail.com
