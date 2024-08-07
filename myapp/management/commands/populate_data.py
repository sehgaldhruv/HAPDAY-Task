import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import AppleHealthStat
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'populate the db with random AppleHealthStat data for any user'

    def handle(self, *args, **kwargs):
        self.create_users_and_stats()

    def create_users_and_stats(self):
        # Create 10 users
        for i in range(10):
            username = f'user{i}'
            if User.objects.filter(username=username).exists():
                self.stdout.write(f'User {username} already exists. Skipping creation.')
                user = User.objects.get(username=username)
            else:
                user = User.objects.create_user(username=username, password='password')
                self.stdout.write(f'User {username} created.')

            for _ in range(25):
                self.create_stats_for_user(user)

    def create_stats_for_user(self, user):
        random_date = datetime.now() - timedelta(days=random.randint(0, 365))
        random_date = timezone.make_aware(random_date)
        AppleHealthStat.objects.create(
            user=user,
            date_of_birth=random_date,
            height=random.randint(150, 200),
            body_mass=random.randint(50, 100),
            body_fat_percentage=random.randint(10, 30),
            biological_sex=random.choice(['Male', 'Female']),
            activity_move_mode=random.choice(['Walking', 'Running', 'Cycling']),
            step_count=random.randint(1000, 20000),
            basal_energy_burned=random.randint(1000, 3000),
            active_energy_burned=random.randint(100, 1000),
            flights_climbed=random.randint(0, 50),
            apple_exercise_time=random.randint(0, 180),
            apple_move_time=random.randint(0, 1440),
            apple_stand_hour=random.randint(0, 24),
            menstrual_flow=random.choice([None, 'Light', 'Medium', 'Heavy']),
            hk_workout_type_identifier=random.choice(['Workout1', 'Workout2', 'Workout3']),
            heart_rate=random.randint(60, 180),
            oxygen_saturation=random.randint(90, 100),
            mindful_session={"duration": random.randint(1, 60)},
            sleep_analysis={"duration": random.randint(1, 10)}
        )
        self.stdout.write(f'AppleHealthStat for {user.username} created.')
