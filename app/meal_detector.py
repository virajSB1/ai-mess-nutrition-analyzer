from datetime import datetime

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

print("Current Day:", current_day)

print("Current Meal:", current_meal)