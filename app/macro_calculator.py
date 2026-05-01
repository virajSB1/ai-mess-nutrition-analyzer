import pandas as pd

food_df = pd.read_csv("../data/food_nutrition.csv")
menu_df = pd.read_csv("../data/mess_menu.csv")

current_day = "Monday"
current_meal = "Lunch"

meal_items = menu_df[
    (menu_df["day"] == current_day) &
    (menu_df["meal_type"] == current_meal)
]

total_calories = 0
total_protein = 0
total_carbs = 0
total_fat = 0

print(f"\n{current_day} {current_meal}\n")

for item in meal_items["food_item"]:

    nutrition = food_df[
        food_df["food_name"] == item
    ]

    if not nutrition.empty:

        calories = nutrition.iloc[0]["calories"]
        protein = nutrition.iloc[0]["protein_g"]
        carbs = nutrition.iloc[0]["carbs_g"]
        fat = nutrition.iloc[0]["fat_g"]

        total_calories += calories
        total_protein += protein
        total_carbs += carbs
        total_fat += fat

        print(item)

print("\nMeal Macros")

print("Calories:", total_calories)
print("Protein:", total_protein, "g")
print("Carbs:", total_carbs, "g")
print("Fat:", total_fat, "g")