from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import AppleHealthStat
from rest_framework.test import APIClient
from rest_framework import status
from datetime import datetime, timedelta

User = get_user_model()

class AppleHealthStatTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.stat = AppleHealthStat.objects.create(
            user=self.user,
            dateOfBirth=datetime.now(),
            height=180,
            bodyMass=75,
            bodyFatPercentage=20,
            biologicalSex='male',
            activityMoveMode='activeEnergy',
            stepCount=10000,
            basalEnergyBurned=1000,
            activeEnergyBurned=500,
            flightsClimbed=10,
            appleExerciseTime=30,
            appleMoveTime=40,
            appleStandHour=8,
            heartRate=60,
            oxygenSaturation=98,
            mindfulSession='{}',
            sleepAnalysis='[{"date": "2024-07-20 04:35", "sleep_time": 1500.264121055603}]'
        )

    def test_sleep_condition(self):
        response = self.client.get('/api/sleep-condition/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_steps_condition_today(self):
        response = self.client.get('/api/steps-condition-today/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_steps_condition_week(self):
        response = self.client.get('/api/steps-condition-week/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
