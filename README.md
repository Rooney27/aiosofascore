![PyPI Version](https://img.shields.io/pypi/v/aiosofascore)
![LICENSE](https://img.shields.io/badge/License-MIT-blue.svg)

# Aiosofascore

**Aiosofascore** is an API client for SofaScore's soccer data, designed to provide easy access to soccer categories, tournaments, events, and much more. It is built with `aiohttp` for asynchronous HTTP requests and can be integrated into any Python project that needs soccer-related data.

## Features

- Fetch soccer categories and tournaments
- Get detailed tournament standings and seasons
- Retrieve pregame forms, head-to-head stats, and event managers
- Built using Python's asynchronous capabilities with `aiohttp`

## Installation

To install **aiosofascore** from PyPI, run the following command:

```bash
pip install aiosofascore

```
## Usage Example

Here's how you can use aiosofascore to get data about football tournaments

```python
import asyncio
from aiosofascore import BaseSoccerApi


async def main():
    # Create a client
    client = BaseSoccerApi()

    # Fetch categories
    categories = await client.get_categories()
    for category in categories:
        print(f"Category: {category.name}")

    # Fetch tournaments by category
    tournaments = await client.get_tournaments_by_category(categories[0])
    for tournament in tournaments:
        print(f"Tournament: {tournament.name}")


if __name__ == "__main__":
    asyncio.run(main())
```

Get event data

```python
import asyncio
from aiosofascore import BaseSoccerApi


async def main():
    
    client = BaseSoccerApi()
    event = await client.get_event(event_id='13363911')
    print(event.home_team.name)
    print(event.away_team.name)


if __name__ == "__main__":
    asyncio.run(main())
```


## License
This project is licensed under the MIT License — see the LICENSE file for details.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact me via vasilewskij.fil@gmail.com
