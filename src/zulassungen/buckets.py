def age_bucket(age: int) -> str:
    if age < 30:
        return "less_than_30"
    elif age < 40:
        return "30_to_less_than_40"
    elif age < 50:
        return "40_to_less_than_50"
    elif age < 60:
        return "50_to_less_than_60"
    elif age < 70:
        return "60_to_less_than_70"
    elif age < 80:
        return "70_to_less_than_80"
    else:
        return "equal_to_or_greater_than_80"


def bmi_bucket(bmi: float) -> str:
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25.0:
        return "healthy_weight"
    elif bmi < 30.0:
        return "overweight"
    elif bmi < 35.0:
        return "obesity_class_1"
    elif bmi < 40.0:
        return "obesity_class_2"
    else:
        return "obesity_class_3"