from typing import Iterable
from kedro.pipeline import node, pipeline
from kedro.runner import SequentialRunner


def mean(x: Iterable[float], n: int) -> float:
    return sum(x) / n


variance_pipeline = pipeline([
    node(func=mean, inputs=["x", "n"], outputs="mean")
])


