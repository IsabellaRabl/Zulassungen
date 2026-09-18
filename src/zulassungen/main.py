import pandas as pd
from pathlib import Path

from zulassungen.buckets import age_bucket, bmi_bucket
from zulassungen.schema.demographics import DemographicsSchema
from zulassungen.validate_json import validate_json
from zulassungen.cross_validation import validate_observers

from zulassungen.extract import extract_folder

def main() -> None:
    #extract_folder(Path("resources/sample_data/VerificationReports_UWS71_00.7z"), Path("output/extracted"))

    print("1) READ DEMOGRAPHICS + VALIDATE (Pandera -> typecheck, plausibility)")
    raw_df = pd.read_csv("resources/sample_data/demographics_example.txt", sep=";")
    demographics = DemographicsSchema.validate(raw_df)
    print(f"{len(demographics)} Successfully validated.\n")

    print("2) BUCKETS")
    demographics["age_bucket"] = demographics["age"].apply(age_bucket)
    demographics["bmi_bucket"] = demographics["bmi_in_kg_per_m2"].apply(bmi_bucket)
    print(demographics[["age", "age_bucket", "bmi_in_kg_per_m2", "bmi_bucket"]])
    print()

    print("3) JSON VALIDATION (Pydantic)")
    try:
        metadata = validate_json(Path("output/extracted/AutomaticMeasurements/final_results_automm_merged_info.json"))
        print("JSON is valid.")
        print(metadata)

    except Exception as e:
        print("JSON is not valid:")
        print(e)
    print()

    print("4) CROSS VALIDATION (csv <-> json)")
    csv_df = pd.read_csv("output/extracted/AutomaticMeasurements/final_results_automm_merged.csv")
    print(csv_df.columns.tolist())
    if validate_observers(csv_df, metadata):
        print("Observer validation passed.")
    else:
        print("Observer validation failed.")
    print()





if __name__ == "__main__":
    main()