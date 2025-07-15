import pytest
import asyncio
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest_asyncio
from aiosofascore.client import SofaScoreClient

TEAM_ID = 2819
PAGE = 0
BASE_URL = "http://api.sofascore.com"

@pytest_asyncio.fixture(scope="module")
async def client():
    client = SofaScoreClient(BASE_URL)
    yield client

@pytest.mark.asyncio
async def test_get_team_info(client):
    info = await client.team.info.get_team_info(TEAM_ID)
    print(info)
    assert info.id == TEAM_ID
    assert info.name
    assert info.slug

@pytest.mark.asyncio
async def test_get_team_players(client):
    players = await client.team.players.get_team_players(TEAM_ID)
    assert players.players is None or isinstance(players.players, list)

@pytest.mark.asyncio
async def test_get_team_performance(client):
    perf = await client.team.performance.get_team_performance(TEAM_ID)
    assert hasattr(perf, "events")
    assert hasattr(perf, "points")

@pytest.mark.asyncio
async def test_get_team_rankings(client):
    rankings = await client.team.rankings.get_team_rankings(TEAM_ID)
    assert rankings is not None
    assert hasattr(rankings, "rankings")

@pytest.mark.asyncio
async def test_get_team_transfers(client):
    transfers = await client.team.transfers.get_team_transfers(TEAM_ID)
    assert hasattr(transfers, "transfersIn")
    assert hasattr(transfers, "transfersOut")

@pytest.mark.asyncio
async def test_get_team_last_events(client):
    last_events = await client.team.last_events.get_last_events(TEAM_ID, PAGE)
    assert hasattr(last_events, "events")
    assert hasattr(last_events, "hasNextPage") 