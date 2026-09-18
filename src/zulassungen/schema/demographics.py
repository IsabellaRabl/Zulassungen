import pandera.pandas as pa
from pandera.typing import Series


class DemographicsSchema(pa.DataFrameModel):
    study_uid: Series[str]
    age: Series[int] = pa.Field(ge=0, le=120)
    gender: Series[str] = pa.Field(isin=["M", "F"])
    height_in_cm: Series[float] = pa.Field(gt=0)
    weight_in_kg: Series[float] = pa.Field(gt=0)
    bmi_in_kg_per_m2: Series[float] = pa.Field(gt=0)
    bsa_in_m2: Series[float] = pa.Field(gt=0)
    ethnicity: Series[str]
    pathologies: Series[str]
