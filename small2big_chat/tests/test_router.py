import sys
import asyncio
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import pytest

from small2big_chat.api.router import route_query


@pytest.mark.parametrize(
    'query',
    [
        'invest in AAPL',
        'consumer spending',
        'labor market stats',
        'signal fusion test',
    ],
)
def test_route_query(query):
    reply, meta = asyncio.run(route_query(query))
    assert isinstance(reply, str) and reply
    assert isinstance(meta, dict)
