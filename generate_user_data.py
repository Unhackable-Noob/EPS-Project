import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Read the original data
df = pd.read_csv('fitness_tracker_data.csv')

# Function to generate realistic health data
def generate_health_data(num_records, base_values):
    data = []
    for _ in range(num_records):
        # Generate slightly varied values around the base values
        record = {
            'Max_BPM': int(np.random.normal(base_values['Max_BPM'], 5)),
            'Avg_BPM': int(np.random.normal(base_values['Avg_BPM'], 3)),
            'Resting_BPM': int(np.random.normal(base_values['Resting_BPM'], 2)),
            'Session_Duration (hours)': round(np.random.normal(base_values['Session_Duration'], 0.2), 2),
            'Calories_Burned': int(np.random.normal(base_values['Calories_Burned'], 100)),
            'Workout_Type': np.random.choice(['Strength', 'Cardio', 'HIIT', 'Yoga']),
            'Fat_Percentage': round(np.random.normal(base_values['Fat_Percentage'], 2), 1),
            'Water_Intake (liters)': round(np.random.normal(base_values['Water_Intake'], 0.3), 1),
            'Workout_Frequency (days/week)': int(np.random.normal(base_values['Workout_Frequency'], 0.5)),
            'Experience_Level': int(np.random.normal(base_values['Experience_Level'], 0.3)),
            'BMI': round(np.random.normal(base_values['BMI'], 1), 2)
        }
        # Ensure values are within reasonable ranges
        record['Max_BPM'] = max(150, min(200, record['Max_BPM']))
        record['Avg_BPM'] = max(120, min(180, record['Avg_BPM']))
        record['Resting_BPM'] = max(50, min(80, record['Resting_BPM']))
        record['Session_Duration (hours)'] = max(0.5, min(2.5, record['Session_Duration (hours)']))
        record['Calories_Burned'] = max(400, min(2000, record['Calories_Burned']))
        record['Fat_Percentage'] = max(10, min(35, record['Fat_Percentage']))
        record['Water_Intake (liters)'] = max(1.5, min(4.0, record['Water_Intake (liters)']))
        record['Workout_Frequency (days/week)'] = max(2, min(7, record['Workout_Frequency (days/week)']))
        record['Experience_Level'] = max(1, min(3, record['Experience_Level']))
        data.append(record)
    return pd.DataFrame(data)

# User 1: Based on a young male athlete
user1_base = {
    'Max_BPM': 190,
    'Avg_BPM': 160,
    'Resting_BPM': 60,
    'Session_Duration': 1.5,
    'Calories_Burned': 1200,
    'Fat_Percentage': 15,
    'Water_Intake': 3.0,
    'Workout_Frequency': 5,
    'Experience_Level': 2,
    'BMI': 22.0
}

# User 2: Based on a middle-aged female fitness enthusiast
user2_base = {
    'Max_BPM': 175,
    'Avg_BPM': 145,
    'Resting_BPM': 65,
    'Session_Duration': 1.2,
    'Calories_Burned': 800,
    'Fat_Percentage': 25,
    'Water_Intake': 2.5,
    'Workout_Frequency': 4,
    'Experience_Level': 2,
    'BMI': 24.0
}

# Generate data for both users
user1_data = generate_health_data(900, user1_base)
user2_data = generate_health_data(900, user2_base)

# Save the data
user1_data.to_csv('user1_health_data.csv', index=False)
user2_data.to_csv('user2_health_data.csv', index=False)

# Print user profiles
print("\nUser 1 Profile:")
print("Age: 25 years")
print("Gender: Male")
print("Weight: 75 kg")
print("Height: 1.85 m")

print("\nUser 2 Profile:")
print("Age: 35 years")
print("Gender: Female")
print("Weight: 65 kg")
print("Height: 1.65 m") 