import pandas as pd

from datetime import datetime

food_df = pd.read_csv("../data/food_nutrition.csv")

menu_df = pd.read_csv("../data/mess_menu.csv")

now = datetime.now()

current_day = now.strftime("%A")

current_hour = now.hour

if 6 <= current_hour < 11:
    current_meal = "Breakfast"

elif 12 <= current_hour < 16:
    current_meal = "Lunch"

elif 19 <= current_hour < 23:
    current_meal = "Dinner"

else:
    current_meal = "No Active Meal"

print("\nCurrent Day:", current_day)

print("Current Meal:", current_meal)

if current_meal == "No Active Meal":

    print("\nNo meal is active right now.")

else:

    meal_items = menu_df[
        (menu_df["day"] == current_day) &
        (menu_df["meal_type"] == current_meal)
    ]

    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    print("\nFoods:\n")

    for item in meal_items["food_item"]:

        print("-", item)

        nutrition = food_df[
            food_df["food_name"] == item
        ]

        if not nutrition.empty:

            total_calories += nutrition.iloc[0]["calories"]

            total_protein += nutrition.iloc[0]["protein_g"]

            total_carbs += nutrition.iloc[0]["carbs_g"]

            total_fat += nutrition.iloc[0]["fat_g"]

    print("\nMeal Macros\n")

    print("Calories:", total_calories)

    print("Protein:", total_protein, "g")

    print("Carbs:", total_carbs, "g")

    print("Fat:", total_fat, "g")