import pandas as pd

food_df = pd.read_csv("../data/food_nutrition.csv")
menu_df = pd.read_csv("../data/mess_menu.csv")

food_items = set(food_df["food_name"])

missing = []

for item in menu_df["food_item"].unique():

    if item not in food_items:
        missing.append(item)

if len(missing) == 0:
    print("All menu items exist in nutrition dataset")

else:
    print("Missing foods:")

    for item in missing:
        print(item)