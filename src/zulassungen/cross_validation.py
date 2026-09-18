import pandas as pd

from zulassungen.validate_json import Metadata


def validate_observers(df: pd.DataFrame, metadata: Metadata) -> bool:
    valid_observer_ids = set(metadata.map_observer_name_to_id.values())
    invalid_observers = set(df["Observer"]) - valid_observer_ids

    if invalid_observers:
        print( f"Invalid observer IDs found in CSV: {invalid_observers}")
        return False

    return True