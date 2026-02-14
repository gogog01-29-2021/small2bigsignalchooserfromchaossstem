import json
from pathlib import Path
from typing import Any, Dict, List


class DummyIndex:
    def __init__(self) -> None:
        self.vectors: List[List[float]] = []

    def add(self, vector: List[float]) -> None:
        self.vectors.append(vector)


INDEX = DummyIndex()


def maybe_log(text: str, meta: Dict[str, Any]) -> None:
    """Log text and meta information."""
    log_path = Path('manus_rules.jsonl')
    with log_path.open('a') as f:
        f.write(json.dumps({'text': text, 'meta': meta}) + '\n')

    embedding = [float(len(text))]
    INDEX.add(embedding)
