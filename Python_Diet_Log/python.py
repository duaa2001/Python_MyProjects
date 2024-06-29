import pandas as pd
import numpy as np 

def main():
    activity_data = pd.read_excel("/Users/duaatariq/Desktop/Git/Python_Diet_log/myenv/activity_data.xlsx", usecols=['Exercise', 'Calories burned per minute'])
    print(activity_data)

    food_log = pd.DataFrame(columns=['Food', 'Calories'])
    exercise_log = pd.DataFrame(columns=['Activity', 'Duration', 'Calories Burned'])

    while True:
        choice = input("Enter your choice (Food/Activity/Total Calories/Exit): ")

        if choice == 'Food':
            food_log =calories_intake(food_log)
            print(food_log)
        elif choice == 'Activity':
            print(activity_data)
            exercise_log= calories_burned(exercise_log, activity_data)
            print(exercise_log)
        elif choice == 'Total Calories':
            print("Total Daily Calories: {}".format(calculate_daily_total(food_log, exercise_log)))
        elif choice == 'Exit':
            print("Exiting program...")
            break
        else:
            print("Invalid. Please try again.")

def calories_intake(food_log):
    food = input("Enter food item: ")
    calories = float(input("Enter calories: "))
    
    new_index = len(food_log)
    food_log.loc[new_index] = [food, calories]

    print("Successful Entry.")
    return food_log

def calories_burned(exercise_log, activity_data):
    activity = input("Enter exercise activity: ")
    duration = float(input("Enter duration (in  minutes): "))

    if activity not in activity_data['Exercise'].values:
        print(f"'{activity}' not found in the activity data.")
    else:
        calories_per_minute = activity_data.loc[activity_data['Exercise'] == activity, 'Calories burned per minute'].values[0]
        calories_burned = calories_per_minute * duration
        
        new_index = len(exercise_log)
        exercise_log.loc[new_index] = [activity, duration, calories_burned]

        print("Successful Entry.")
        
    return exercise_log

def calculate_daily_total(food_log, exercise_log):
    total_calories_intake = np.sum(food_log['Calories'])
    total_calories_burned = np.sum(exercise_log['Calories Burned'])
    total_calories_daily =  total_calories_intake - total_calories_burned
    return total_calories_daily

if __name__ == "__main__":
    main()