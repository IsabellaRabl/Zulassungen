from pydantic import BaseModel
from pathlib import Path

class Metadata(BaseModel):
    map_observer_name_to_id: dict[str, int]
    map_pool_name_to_id: dict[str, int]
    folders: list[str]

def validate_json(json_path: Path):
    json_data = json_path.read_text(encoding="utf-8")
    return Metadata.model_validate_json(json_data)