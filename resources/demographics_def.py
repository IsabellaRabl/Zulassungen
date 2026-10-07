if buckets_variant == "detailed":
    current_age = int(current_study["age"])
    if current_age < 30:
        age_bucket = "less_than_30"
    elif current_age < 40:
        age_bucket = "30_to_less_than_40"
    elif current_age < 50:
        age_bucket = "40_to_less_than_50"
    elif current_age < 60:
        age_bucket = "50_to_less_than_60"
    elif current_age < 70:
        age_bucket = "60_to_less_than_70"
    elif current_age < 80:
        age_bucket = "70_to_less_than_80"
    else:
        age_bucket = "equal_to_or_greater_than_80"

    current_bmi = float(current_study["bmi_in_kg_per_m2"])
    if current_bmi < 18.5:
        bmi_bucket = "underweight"
    elif current_bmi < 25.0:
        bmi_bucket = "healthy_weight"
    elif current_bmi < 30.0:
        bmi_bucket = "overweight"
    elif current_bmi < 35.0:
        bmi_bucket = "obesity_class_1"
    elif current_bmi < 40.0:
        bmi_bucket = "obesity_class_2"
    else:
        bmi_bucket = "obesity_class_3"