import pandas as pd

from zulassungen.validate_json import Metadata


def validate_observers(df: pd.DataFrame, metadata: Metadata) -> bool:
    """
    Step 4 - Cross Validation CSV <-> JSON
    -> used to cross-validate the Metadata-Model and
        output/extracted/AutomaticMeasurements/final_results_automm_merged.csv
    """
    valid_observer_ids = set(metadata.map_observer_name_to_id.values())
    invalid_observers = set(df["Observer"]) - valid_observer_ids

    if invalid_observers:
        print( f"Invalid observer IDs found in CSV: {invalid_observers}")
        return False

    return True