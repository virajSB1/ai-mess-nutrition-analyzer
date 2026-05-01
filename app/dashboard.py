import streamlit as st

import pandas as pd

from sklearn.tree import DecisionTreeClassifier

from datetime import datetime

st.set_page_config(
    page_title="AI Mess Nutrition Analyzer",
    page_icon="🍽️",
    layout="centered"
)

food_df = pd.read_csv("data/food_nutrition.csv")

menu_df = pd.read_csv("data/mess_menu.csv")

labels_df = pd.read_csv(
    "data/meal_health_labels.csv",
    sep="\t"
)

X = labels_df[
    [
        "calories",
        "protein",
        "carbs",
        "fat",
        "fiber"
    ]
]

y = labels_df["label"]

model = DecisionTreeClassifier()

model.fit(X, y)

now = datetime.now()

current_day = now.strftime("%A")

mode = st.sidebar.selectbox(
    "Mode",
    ["Auto Detect", "Manual"]
)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    [
        "Weight Loss",
        "Maintenance",
        "Muscle Gain"
    ]
)

if mode == "Auto Detect":

    current_minutes = (
        now.hour * 60
        +
        now.minute
    )

    breakfast_start = 7 * 60 + 30
    breakfast_end = 9 * 60 + 30

    lunch_start = 12 * 60
    lunch_end = 14 * 60

    dinner_start = 19 * 60 + 30
    dinner_end = 21 * 60

    if breakfast_start <= current_minutes < breakfast_end:
        current_meal = "Breakfast"

    elif lunch_start <= current_minutes < lunch_end:
        current_meal = "Lunch"

    elif dinner_start <= current_minutes < dinner_end:
        current_meal = "Dinner"

    else:
        st.warning("No active meal time right now.")
        st.stop()

else:

    current_day = st.sidebar.selectbox(
        "Select Day",
        menu_df["day"].unique()
    )

    current_meal = st.sidebar.selectbox(
        "Select Meal",
        ["Breakfast", "Lunch", "Dinner"]
    )

meal_items = menu_df[
    (menu_df["day"] == current_day)
    &
    (menu_df["meal_type"] == current_meal)
]

total_calories = 0
total_protein = 0
total_carbs = 0
total_fat = 0
total_fiber = 0

st.title("🍽️ AI Mess Nutrition Analyzer")

st.caption(
    "Smart AI-powered mess meal analysis system"
)

st.subheader(
    f"{current_day} - {current_meal}"
)

for item in meal_items["food_item"]:

    nutrition = food_df[
        food_df["food_name"] == item
    ]

    if not nutrition.empty:

        row = nutrition.iloc[0]

        st.markdown(f"### 🍛 {item}")

        st.info(
            f"Calories: {row['calories']} | "
            f"Protein: {row['protein_g']}g | "
            f"Carbs: {row['carbs_g']}g | "
            f"Fat: {row['fat_g']}g"
        )

        total_calories += row["calories"]

        total_protein += row["protein_g"]

        total_carbs += row["carbs_g"]

        total_fat += row["fat_g"]

        total_fiber += row["fiber_g"]

st.subheader("Meal Macros")

st.write(f"Calories: {total_calories}")

st.write(f"Protein: {total_protein}g")

st.write(f"Carbs: {total_carbs}g")

st.write(f"Fat: {total_fat}g")

st.write(f"Fiber: {total_fiber}g")

prediction = model.predict(pd.DataFrame([{
    "calories": total_calories,
    "protein": total_protein,
    "carbs": total_carbs,
    "fat": total_fat,
    "fiber": total_fiber
}]))

st.subheader("AI Analysis")

st.success(prediction[0])

st.subheader("Recommendations")

if goal == "Weight Loss":

    if total_calories > 700:
        st.warning(
            "High calorie meal for weight loss"
        )

    if total_fat > 25:
        st.warning(
            "Fat content is high"
        )

if goal == "Muscle Gain":

    if total_protein < 35:
        st.warning(
            "Protein intake is low for muscle gain"
        )

    else:
        st.success(
            "Good protein intake for muscle gain"
        )

if goal == "Maintenance":

    st.info(
        "Balanced intake recommended"
    )
