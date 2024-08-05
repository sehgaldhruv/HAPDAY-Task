from django.urls import path
from .views import sleep_condition, steps_condition_today, steps_condition_week

urlpatterns = [
    path('conditions/sleep/', sleep_condition),
    path('conditions/steps_today/', steps_condition_today),
    path('conditions/steps_week/', steps_condition_week),
]
