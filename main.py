import asyncio

from sofascore.api.soccer.base import BaseSoccerApi


async def main():
    api_client = BaseSoccerApi()
    print(await api_client.get_categories())

if __name__ == '__main__':
    asyncio.run(main())