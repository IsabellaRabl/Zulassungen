import pandas as pd
from pathlib import Path

from zulassungen.buckets import age_bucket, bmi_bucket
from zulassungen.schema.demographics import DemographicsSchema
from zulassungen.schema.merged_results import MergedResultsSchema
from zulassungen.validate_json import validate_json
from zulassungen.cross_validation import validate_observers

from zulassungen.extract import extract_folder

def main() -> None:
    # Diese Zeile nur einkommentieren wenn die .7z neu extrahiert werden soll
    #extract_folder(Path("resources/VerificationReports_UWS71_00.7z"), Path("output/extracted"))

    print("\n" + "-" * 50)
    print("1) READ DEMOGRAPHICS + VALIDATE (Pandera -> typecheck, plausibility)")
    raw_df = pd.read_csv("resources/demographics_example.txt", sep=";")
    demographics = DemographicsSchema.validate(raw_df)
    print(f"{len(demographics)} Successfully validated.")

    print("\n" + "-" * 50)
    print("1.1) VALIDATION AFTER ASSIGNMENT (Pandera)")
    try:
        demographics.loc[0, "age"] = 150
        DemographicsSchema.validate(demographics)
        print("An incorrect assignment was accepted by mistake!")
    except Exception as e:
        print("The incorrect assignment was correctly rejected:")
        print(e)

    print("\n" + "-" * 50)
    print("2) BUCKETS")
    demographics["age_bucket"] = demographics["age"].apply(age_bucket)
    demographics["bmi_bucket"] = demographics["bmi_in_kg_per_m2"].apply(bmi_bucket)
    print(demographics[["age", "age_bucket", "bmi_in_kg_per_m2", "bmi_bucket"]])

    print("\n" + "-" * 50)
    print("3) JSON VALIDATION (Pydantic)")
    try:
        metadata = validate_json(Path("output/extracted/AutomaticMeasurements/final_results_automm_merged_info.json"))
        print("JSON is valid.")
        print(metadata)

    except Exception as e:
        print("JSON is not valid:")
        print(e)

    print("\n" + "-" * 50)
    print("3.1) VALIDATE_ASSIGNMENT DEMO (Pydantic validates after creation)")
    try:
        metadata.map_observer_name_to_id = "incorrect value" # type: ignore
        print("An incorrect assignment was accepted by mistake!")
    except Exception as e:
        print("The incorrect assignment was correctly rejected:")
        print(e)

    print("\n" + "-" * 50)
    print("4) CROSS VALIDATION (CSV <-> JSON)")
    csv_df = pd.read_csv("output/extracted/AutomaticMeasurements/final_results_automm_merged.csv")
    print(csv_df.columns.tolist())
    if validate_observers(csv_df, metadata):
        print("Observer validation passed.")
    else:
        print("Observer validation failed.")

    print("\n" + "-" * 50)
    print("5) MERGED RESULTS VALIDATION")
    try:
        valid_results = MergedResultsSchema.validate(csv_df)
        print(f"{len(valid_results)} lines validated.\n")
    except Exception as e:
        print("Validation failed:")
        print(e)

    print("\n" + "-" * 50)
    print("6) MEAN OBSERVER")
    mean = valid_results.groupby(["Exam ID", "Parameter"])["Automated output (AutoMM measurement without ECG on detected frame)"].mean()
    print(mean)





if __name__ == "__main__":
    main()