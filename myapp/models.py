# myapp/models.py
from django.contrib.auth import get_user_model
from django.db import models

class AppleHealthStat(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='apple_health_stat')
    date_of_birth = models.DateTimeField(null=True, blank=True)
    height = models.PositiveSmallIntegerField(null=True, blank=True)
    body_mass = models.PositiveSmallIntegerField(null=True, blank=True)
    body_fat_percentage = models.PositiveSmallIntegerField(null=True, blank=True)
    biological_sex = models.CharField(max_length=32, null=True, blank=True)
    activity_move_mode = models.CharField(max_length=128, null=True, blank=True)
    step_count = models.PositiveSmallIntegerField(null=True, blank=True)
    basal_energy_burned = models.PositiveSmallIntegerField(null=True, blank=True)
    active_energy_burned = models.PositiveSmallIntegerField(null=True, blank=True)
    flights_climbed = models.PositiveSmallIntegerField(null=True, blank=True)
    apple_exercise_time = models.PositiveSmallIntegerField(null=True, blank=True)
    apple_move_time = models.PositiveSmallIntegerField(null=True, blank=True)
    apple_stand_hour = models.PositiveSmallIntegerField(null=True, blank=True)
    menstrual_flow = models.CharField(max_length=128, null=True, blank=True)
    hk_workout_type_identifier = models.CharField(max_length=128, null=True, blank=True)
    heart_rate = models.PositiveSmallIntegerField(null=True, blank=True)
    oxygen_saturation = models.PositiveSmallIntegerField(null=True, blank=True)
    mindful_session = models.JSONField(null=True, blank=True)
    sleep_analysis = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
