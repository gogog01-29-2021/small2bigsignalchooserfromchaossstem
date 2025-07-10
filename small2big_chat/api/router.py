from typing import Tuple, Dict

from ..core.bellman_invest import run as bellman_invest
from ..core.deep_iv_consumer import run as deep_iv_consumer
from ..core.psid_labor import run as psid_labor
from ..core.signal_fusion import run as signal_fusion
from ..agents.manus import maybe_log


async def route_query(query: str) -> Tuple[str, Dict]:
    """Route the query to the appropriate handler."""
    q = query.lower()
    if "invest" in q or "bellman" in q:
        reply, meta = await bellman_invest("demo")
    elif "consumer" in q:
        reply, meta = await deep_iv_consumer()
    elif "labor" in q or "psid" in q:
        reply, meta = await psid_labor()
    elif "fuse" in q or "signal" in q:
        reply, meta = await signal_fusion({"a": 0.1, "b": 0.2})
    else:
        reply, meta = await psid_labor()

    maybe_log(query, meta)
    return reply, meta
