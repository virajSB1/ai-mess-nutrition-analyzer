import pandas as pd

df = pd.read_excel(
    r"C:\STORAGE\AI MESS NUTRITION PROJECT\menu.xlsx",
    header=1
)

menu_data = []

for _, row in df.iterrows():

    day = str(row["DAY"]).strip()

    meals = {
        "Breakfast": row["BREAKFAST"],
        "Lunch": row["LUNCH"],
        "Dinner": row["DINNER"]
    }

    for meal_type, foods in meals.items():

        if pd.isna(foods):
            continue

        food_list = str(foods).split(",")

        for food in food_list:

            cleaned_food = food.strip()

            if cleaned_food:

                menu_data.append([
                    day.title(),
                    meal_type,
                    cleaned_food
                ])

menu_df = pd.DataFrame(
    menu_data,
    columns=[
        "day",
        "meal_type",
        "food_item"
    ]
)

menu_df.to_csv(
    r"C:\STORAGE\AI MESS NUTRITION PROJECT\data\mess_menu.csv",
    index=False
)

print("mess_menu.csv updated successfully")