import pandas as pd
import pandera.pandas as pa
from pandera.typing import Series


class MergedResultsSchema(pa.DataFrameModel):
    """Schema for AutomaticMeasurements/final_results_autom_merged.csv."""
    pool: Series[int] = pa.Field(alias="Pool")
    observer: Series[int] = pa.Field(alias="Observer")
    exam_id: Series[str] = pa.Field(alias="Exam ID")
    parameter: Series[str] = pa.Field(alias="Parameter")
    automated_output: Series[float] = pa.Field(alias="Automated output (AutoMM measurement without ECG on detected frame)")

    @pa.dataframe_check
    def one_measurement_per_observer(cls, df: pd.DataFrame) -> bool:
        count = df.groupby(["Exam ID", "Observer", "Parameter"]).size()
        result = (count == 1).all()
        return bool(result)