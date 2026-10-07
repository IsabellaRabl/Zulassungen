from pydantic import BaseModel, ConfigDict
from pathlib import Path

class Metadata(BaseModel):
    """
    Step 3 and 3.1 - Pydantic Validation
    -> used on output/extracted/AutomaticMeasurements/final_results_automm_merged_info.json
    """
    model_config = ConfigDict(validate_assignment=True)

    map_observer_name_to_id: dict[str, int]
    map_pool_name_to_id: dict[str, int]
    folders: list[str]

def validate_json(json_path: Path):
    json_data = json_path.read_text(encoding="utf-8")
    return Metadata.model_validate_json(json_data)