# HAPDAY-Task

# Health Data Analysis API

This API provides personalized health insights based on user data from the Apple Health SDK. The following conditions are checked:

- **Sleep Condition**: Users with less than 6 hours of sleep in the past week.
- **Steps Condition Today**: Users who have reached 10,000 steps today.
- **Steps Condition Week**: Users who walked 50% less this week compared to the previous week.

## API Endpoints

### Sleep Condition
**Endpoint**: `/conditions/sleep/`


### Steps Condition Today
**Endpoint: /conditions/steps_today/

### Steps Condition Week
**Endpoint**: `/conditions/steps_week/`

**Example Response**:
![Steps Condition Week Example](attachment:example-steps-condition-week.png)

## Installation

1. Clone the repository.
2. Install dependencies:
   pip install -r requirements.txt

##note setup database for app to run properly