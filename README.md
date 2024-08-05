This Django project provides an API to analyze health data and generate personalized advice based on specific conditions. The conditions include sleep analysis and step counts.

## Features

- implimented users with a week of sleep less than 6 hours
- implimented users who have reached 10,000 steps today
- users who walked 50% less this week compared to the previous week
- generate personalized AI responses based on user data

### Prerequisites

- Python 3.x
- Django 3.x or later
- OpenAI API key use my key i have mentioned it in views 

### Installation

1. **Clone the repository:**

2. **Create environment:**

3. **Install dependencies:**

    pip install -r requirements.txt
4. **Configure the database:**
    it is important to open settings.py and configure database settings otherwise error
5. **Run migrations:**

   commands:-
    python manage.py makemigrations
    python manage.py migrate

6. **Create a superuser:**

    python manage.py createsuperuser


7. **Run the development server:**

    python manage.py runserver

## Configuration

### Models

 model is used to store health-related data for users. It includes fields such as step count, sleep analysis, and other health metrics.

**models.py:**

from django.db import models 
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class AppleHealthStat(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='apple_health_stat')
    dateOfBirth = models.DateTimeField(null=True, blank=True)
    height = models.PositiveSmallIntegerField(null=True, blank=True)
    bodyMass = models.PositiveSmallIntegerField(null=True, blank=True)
    bodyFatPercentage = models.PositiveSmallIntegerField(null=True, blank=True)
    biologicalSex = models.CharField(max_length=32, null=True, blank=True)
    activityMoveMode = models.CharField(max_length=128, null=True, blank=True)
    stepCount = models.PositiveSmallIntegerField(null=True, blank=True)
    basalEnergyBurned = models.PositiveSmallIntegerField(null=True, blank=True)
    activeEnergyBurned = models.PositiveSmallIntegerField(null=True, blank=True)
    flightsClimbed = models.PositiveSmallIntegerField(null=True, blank=True)
    appleExerciseTime = models.PositiveSmallIntegerField(null=True, blank=True)
    appleMoveTime = models.PositiveSmallIntegerField(null=True, blank=True)
    appleStandHour = models.PositiveSmallIntegerField(null=True, blank=True)
    menstrualFlow = models.CharField(max_length=128, null=True, blank=True)
    HKWorkoutTypeIdentifier = models.CharField(max_length=128, null=True, blank=True)
    heartRate = models.PositiveSmallIntegerField(null=True, blank=True)
    oxygenSaturation = models.PositiveSmallIntegerField(null=True, blank=True)
    mindfulSession = models.JSONField(null=True, blank=True)
    sleepAnalysis = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)