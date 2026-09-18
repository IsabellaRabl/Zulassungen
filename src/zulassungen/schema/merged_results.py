import pandera.pandas as pa
from pandera.typing import Series


class MergedResultsSchema(pa.DataFrameModel):
    """Schema for AutomaticMeasurements/final_results_autom_merged.csv."""
    pool: Series[int] = pa.Field(alias="Pool")
    observer: Series[int] = pa.Field(alias="Observer")
