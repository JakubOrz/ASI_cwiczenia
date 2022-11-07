from typing import Iterable
from kedro.pipeline import node, pipeline
from kedro.runner import SequentialRunner
from kedro.io import DataCatalog, MemoryDataSet


runner = SequentialRunner()
data_catalog = DataCatalog(feed_dict={"x": [1, 2, 3]})

calculated_mean = runner.run(pipeline=variance_pipeline, catalog=data_catalog)

print(calculated_mean)
