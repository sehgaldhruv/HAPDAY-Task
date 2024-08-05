from django.http import JsonResponse
from django.contrib.auth.models import User
from django.conf import settings
from .models import AppleHealthStat
from datetime import datetime, timedelta
import openai
import json

with open('/mnt/data/apple_health_data.json') as f:
    health_data = json.load(f)


openai.api_key = settings.OPENAI_API_KEY

def calculate_weekly_sleep(sleep_analysis):
    past_week = [datetime.now() - timedelta(days=i) for i in range(7)]
    total_sleep = 0
    for entry in sleep_analysis:
        sleep_date = datetime.strptime(entry['date'], "%Y-%m-%d %H:%M")
        if sleep_date in past_week:
            total_sleep += entry['sleep_time']
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
    for entry in health_data:
        total_sleep = calculate_weekly_sleep(entry['sleep_analysis'])
        if total_sleep < 6 * 3600: 
            users_with_low_sleep.append(entry['user'])

    responses = []
    for user in users_with_low_sleep:
        response_text = get_ai_response(f"Hello, {user}. I noticed you had less than 6 hours of sleep last week. It's important to get enough rest for your overall well-being. Try to establish a regular sleep schedule and create a relaxing bedtime routine.")
        responses.append({"user": user, "ai_response": response_text})

    return JsonResponse(responses, safe=False)


def steps_condition_today(request):
    users_with_steps = [entry['user'] for entry in health_data if entry['step_count'] >= 10000]

    responses = []
    for user in users_with_steps:
        response_text = get_ai_response(f"Hello, {user}. I see that you reached 10,000 steps today! Great job on staying active. Keep up the good work to maintain a healthy lifestyle.")
        responses.append({"user": user, "ai_response": response_text})

    return JsonResponse(responses, safe=False)


def steps_condition_week(request):
    users_with_less_steps = []
    for entry in health_data:
        weekly_steps = sum([analysis['sleep_time'] for analysis in entry['sleep_analysis']])
        previous_week_steps = sum([analysis['sleep_time'] for analysis in entry['sleep_analysis']]) 

        if weekly_steps < previous_week_steps * 0.5:
            users_with_less_steps.append(entry['user'])

    responses = []
    for user in users_with_less_steps:
        response_text = get_ai_response(f"Hello, {user}. I noticed that you walked 50% less this week compared to last week. Try to set small goals and gradually increase your activity levels to stay fit.")
        responses.append({"user": user, "ai_response": response_text})

    return JsonResponse(responses, safe=False)
