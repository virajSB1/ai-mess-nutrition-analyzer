import pandas as pd

import pickle

from datetime import datetime

food_df = pd.read_csv("../data/food_nutrition.csv")

menu_df = pd.read_csv("../data/mess_menu.csv")

with open("../models/meal_classifier.pkl", "rb") as file:
    model = pickle.load(file)

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
    print("\nNo active meal time right now.")
    exit()

print("\nCurrent Day:", current_day)

print("Current Meal:", current_meal)

meal_items = menu_df[
    (menu_df["day"] == current_day) &
    (menu_df["meal_type"] == current_meal)
]

total_calories = 0
total_protein = 0
total_carbs = 0
total_fat = 0
total_fiber = 0

print("\nFoods:\n")

for item in meal_items["food_item"]:

    nutrition = food_df[
        food_df["food_name"] == item
    ]

    if not nutrition.empty:

        print(f"\n{item}")

        print(
            "Calories:",
            nutrition.iloc[0]["calories"],
            "| Protein:",
            nutrition.iloc[0]["protein_g"],
            "| Carbs:",
            nutrition.iloc[0]["carbs_g"],
            "| Fat:",
            nutrition.iloc[0]["fat_g"]
        )

        total_calories += nutrition.iloc[0]["calories"]

        total_protein += nutrition.iloc[0]["protein_g"]

        total_carbs += nutrition.iloc[0]["carbs_g"]

        total_fat += nutrition.iloc[0]["fat_g"]

        total_fiber += nutrition.iloc[0]["fiber_g"]

print("\nMeal Macros\n")

print("Calories:", total_calories)

print("Protein:", total_protein)

print("Carbs:", total_carbs)

print("Fat:", total_fat)

print("Fiber:", total_fiber)

prediction = model.predict(pd.DataFrame([{
    "calories": total_calories,
    "protein": total_protein,
    "carbs": total_carbs,
    "fat": total_fat,
    "fiber": total_fiber
}]))

print("\nAI Analysis:")

print(prediction[0])

print("\nRecommendations:\n")

if total_protein < 25:
    print("- Protein is low")

if total_carbs > 100:
    print("- High carbohydrate meal")

if total_fat > 35:
    print("- High fat content")

if total_fiber < 5:
    print("- Low fiber intake")

if total_protein >= 35:
    print("- Good protein content")