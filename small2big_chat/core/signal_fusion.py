from typing import Dict, Tuple


async def run(signals: Dict[str, float]) -> Tuple[str, Dict]:
    risk = sum(signals.values()) / (len(signals) + 1)
    return f"Risk score: {risk:.2f}", {"risk": risk}
