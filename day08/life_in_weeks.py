weeks_in_year = 52
human_life_in_years = 90
human_life_in_weeks = human_life_in_years * weeks_in_year

def life_in_weeks(age):
    enjoy_weeks = age * weeks_in_year
    left_weeks = human_life_in_weeks - enjoy_weeks
    print(f"You have {left_weeks} weeks left.")


# Calling function with hard coded current age
life_in_weeks(56)