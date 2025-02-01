import asyncio

from sofascore.api.soccer.base import BaseSoccerApi


async def main():
    api_client = BaseSoccerApi()
    api_client.
    print(await api_client.get_categories())

if __name__ == '__main__':
    asyncio.run(main())