import csv
from faker import Faker
from datetime import datetime, timedelta
import random

# Initializing Faker instance
fake = Faker()

# Specify the number of rows to be generated
num_rows = random.randint(800,1000)

# Define the possible values for some of the columns
live_or_on_demand_choices = ['live', 'on_demand']
subscribed_status_choices = ['subscribed', 'not_subscribed']
country_code_choices = ['US', 'CN', 'FR', 'ZZ']  # you can add more country codes if needed
age_group_choices = ['AGE_18_24', 'AGE_25_34', 'AGE_35_44', 'AGE_45_54', 'AGE_55_64', 'AGE_65_']
gender_choices = ['MALE', 'FEMALE']

# Define the header
header = ['date', 'channel_id', 'video_id', 'live_or_on_demand', 'subscribed_status', 'country_code', 'age_group', 'gender', 'views_percentage']

# Open a file in write mode
with open('p_channel_demographics_a1_channel.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(header)
    
    # Generate and write the random rows
    for _ in range(num_rows):
        date = (datetime.now() - timedelta(days=random.randint(0, 7))).strftime('%Y%m%d')
        channel_id = "b3aae0c1-8e21-4100-9def-5093d454022f"
        video_id = random.choice([
            'cae7a02f-b2b3-4619-ad4d-620f470a7182',
            'a5ce5123-bc8f-432f-af10-5b7046808e77',
            'a5e5043e-d12f-4ebd-aa76-f27de0d1bdbb',
            '723ad3be-64b7-4c4e-8086-85ea199c2979',
            '45fc30f6-2682-42eb-8a7b-cc51d8077c48'
        ])
        live_or_on_demand = random.choice(live_or_on_demand_choices)
        subscribed_status = random.choice(subscribed_status_choices)
        country_code = random.choice(country_code_choices)
        age_group = random.choice(age_group_choices)
        gender = random.choice(gender_choices)
        views_percentage = round(random.uniform(0, 1), 6)
        
        # Write the row
        writer.writerow([date, channel_id, video_id, live_or_on_demand, subscribed_status, country_code, age_group, gender, views_percentage])
