from django.db import models
from django.contrib.auth.models import User

class AppleHealthStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField()
    height = models.IntegerField()
    body_mass = models.IntegerField()
    body_fat_percentage = models.IntegerField()
    biological_sex = models.CharField(max_length=10)
    activity_move_mode = models.CharField(max_length=50)
    step_count = models.IntegerField()
    basal_energy_burned = models.IntegerField()
    active_energy_burned = models.IntegerField()
    flights_climbed = models.IntegerField()
    apple_exercise_time = models.IntegerField()
    apple_move_time = models.IntegerField()
    apple_stand_hour = models.IntegerField()
    menstrual_flow = models.CharField(max_length=50, null=True, blank=True)
    hk_workout_type_identifier = models.CharField(max_length=50)
    heart_rate = models.IntegerField()
    oxygen_saturation = models.IntegerField()
    mindful_session = models.JSONField()
    sleep_analysis = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.date_of_birth}'
