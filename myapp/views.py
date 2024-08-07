from django.http import JsonResponse
from django.contrib.auth.models import User
from django.conf import settings
from .models import AppleHealthStat
from datetime import datetime, timedelta
import openai
import json
import random

openai.api_key = settings.OPENAI_API_KEY

def calculate_weekly_sleep(user):
    past_week = datetime.now() - timedelta(days=7)
    sleep_data = AppleHealthStat.objects.filter(user=user, created_at__gte=past_week)
    total_sleep = sum(entry.sleep_analysis['sleep_time'] for entry in sleep_data if 'sleep_time' in entry.sleep_analysis)
    return total_sleep

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def sleep_condition(request):
    users_with_low_sleep = []
    for user in User.objects.all():
        total_sleep = calculate_weekly_sleep(user)
        if total_sleep < 6 * 3600:  #less then 6hr
            users_with_low_sleep.append(user)

    responses = []
    for user in users_with_low_sleep:
        response_text = get_ai_response(f"Hello, {user.username}. I noticed you had less than 6 hours of sleep last week. It's important to get enough rest for your overall well-being. Try to establish a regular sleep schedule and create a relaxing bedtime routine.")
        responses.append({"user": user.username, "ai_response": response_text})

    return JsonResponse(responses, safe=False)

def steps_condition_today(request):
    today = datetime.now().date()
    users_with_steps = AppleHealthStat.objects.filter(
        created_at__date=today,
        step_count__gte=10000
    ).values_list('user', flat=True).distinct()

    responses = []
    for user_id in users_with_steps:
        user = User.objects.get(id=user_id)
        response_text = get_ai_response(f"Hello, {user.username}. I see that you reached 10,000 steps today! Great job on staying active. Keep up the good work to maintain a healthy lifestyle.")
        responses.append({"user": user.username, "ai_response": response_text})

    return JsonResponse(responses, safe=False)

def get_users_with_steps_condition():
    today = timezone.now().date()
    last_week = today - timedelta(days=7)
    week_before_last = last_week - timedelta(days=7)

    users = User.objects.filter(
        applehealthstat__created_at__gte=week_before_last,
        applehealthstat__created_at__lt=last_week
    ).annotate(
        weekly_steps=models.Sum(
            models.Case(
                models.When(applehealthstat__created_at__gte=last_week, then='applehealthstat__step_count'),
                default=0,
                output_field=models.IntegerField()
            )
        ),
        previous_week_steps=models.Sum(
            models.Case(
                models.When(
                    applehealthstat__created_at__gte=week_before_last,
                    applehealthstat__created_at__lt=last_week,
                    then='applehealthstat__step_count'
                ),
                default=0,
                output_field=models.IntegerField()
            )
        )
    ).filter(weekly_steps__gt=models.F('previous_week_steps'))

    return users

def steps_condition_week(request):
    one_week_ago = datetime.now() - timedelta(days=7)
    two_weeks_ago = datetime.now() - timedelta(days=14)

    users_with_less_steps = []
    for user in User.objects.all():
        current_week_steps = AppleHealthStat.objects.filter(
            user=user,
            created_at__gte=one_week_ago,
            created_at__lt=datetime.now()
        ).aggregate(total_steps=models.Sum('step_count'))['total_steps'] or 0
        
        previous_week_steps = AppleHealthStat.objects.filter(
            user=user,
            created_at__gte=two_weeks_ago,
            created_at__lt=one_week_ago
        ).aggregate(total_steps=models.Sum('step_count'))['total_steps'] or 0

        if current_week_steps < 0.5 * previous_week_steps:
            users_with_less_steps.append(user)

    responses = []
    for user in users_with_less_steps:
        response_text = get_ai_response(f"Hello, {user.username}. i noted that you walked 50% less this week compared to last week. try to set small goals and gradually increase your activity levels to stay fit.")
        responses.append({"user": user.username, "ai_response": response_text})

    return JsonResponse(responses, safe=False)
