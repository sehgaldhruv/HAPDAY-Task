import json
import random
from datetime import datetime, timedelta

users = ["user1", "user2", "user3"]
data = []

for user in users:
    user_data = {
        "user": user,
        "date_of_birth": "1989-08-01",
        "created_at": str(datetime.now()),
        "updated_at": str(datetime.now()),
        "height": random.randint(150, 200),
        "body_mass": random.randint(50, 100),
        "body_fat_percentage": random.randint(10, 30),
        "biological_sex": random.choice(["male", "female"]),
        "activity_move_mode": random.choice(["activeEnergy", "passiveEnergy"]),
        "step_count": random.randint(0, 20000),
        "basal_energy_burned": random.randint(500, 2000),
        "active_energy_burned": random.randint(100, 1000),
        "flights_climbed": random.randint(0, 20),
        "apple_exercise_time": random.randint(0, 60),
        "apple_move_time": random.randint(0, 60),
        "apple_stand_hour": random.randint(0, 24),
        "menstrual_flow": random.choice(["unspecified", "light", "medium", "heavy"]),
        "hk_workout_type_identifier": None,
        "heart_rate": random.randint(60, 100),
        "oxygen_saturation": random.randint(95, 100),
        "mindful_session": "",
        "sleep_analysis": [
            {"date": str(datetime.now() - timedelta(days=i)), "sleep_time": random.randint(1000, 10000)} for i in range(7)
        ]
    }
    data.append(user_data)

with open('apple_health_data.json', 'w') as f:
    json.dump(data, f, indent=4)
