import json
import pytest

import aiohttp
import backoff


@pytest.fixture()
async def aiohht_client():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@backoff.on_exception(
    backoff.expo,
    aiohttp.client_exceptions
)
@pytest.fixture
def make_request(aiohht_client):
    async def inner(method, url, params, args=None):
        response = await aiohht_client.request(
            method,
            url,
            json=params,
            params=args
        )
        return response

    return inner
