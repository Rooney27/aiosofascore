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
- Удобный фасад SofaScoreClient для всех сервисов

## Установка

```bash
pip install aiosofascore
```

## Быстрый старт

### Получить последние события команды
```python
import asyncio
from aiosofascore.client import SofaScoreClient

async def main():
    client = SofaScoreClient(base_url="http://api.sofascore.com/api")
    team_id = 25856
    result = await client.team.last_events.get_last_events(team_id)
    for event in result.events:
        tournament_name = event.tournament.name if event.tournament and event.tournament.name else "-"
        print(f"Event id: {event.id}, турнир: {tournament_name}, дата: {event.startTimestamp}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Пример поиска
```python
import asyncio
from aiosofascore.client import SofaScoreClient

async def main():
    client = SofaScoreClient(base_url="http://api.sofascore.com/api")
    # Поиск менеджеров по имени Alexander
    async for result in client.search.search.search_entities("Alexander", type="manager"):
        name = result.entity.name if result.entity and hasattr(result.entity, 'name') else "-"
        team = result.entity.team.name if result.entity and hasattr(result.entity, 'team') and result.entity.team and hasattr(result.entity.team, 'name') else "-"
        print(f"Имя: {name}, Тип: {result.type}, Команда: {team}")

if __name__ == "__main__":
    asyncio.run(main())
```

## License
This project is licensed under the MIT License — see the LICENSE file for details.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact me via vasilewskij.fil@gmail.com
