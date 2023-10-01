import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Define constants
NUM_ROWS = random.randint(4000, 5000)
FILENAME = "p_channel_traffic_source_a2_channel.csv"
LIVE_OR_ON_DEMAND = ["live", "on_demand"]
SUBSCRIBED_STATUS = ["subscribed", "not_subscribed"]
TRAFFIC_SOURCE_TYPES = list(range(1, 10))  # assuming 1-9 as valid traffic_source_type
TRAFFIC_SOURCE_DETAIL = ["direct", "referral", "unknown", "search"]
COUNTRIES = ['US', 'CN', 'FR', 'GB', 'RU', 'BR', 'IN', 'CA', 'ZA', 'AU', 'ZZ']  # Manually created list of ISO-3166-1 country codes


def generate_row():
    date = (datetime.now() - timedelta(days=random.randint(0, 7))).strftime('%Y%m%d')
    channel_id = "b3aae0c1-8e21-4100-9def-5093d454022f"
    video_id = random.choice([
        'cae7a02f-b2b3-4619-ad4d-620f470a7182',
        'a5ce5123-bc8f-432f-af10-5b7046808e77',
        'a5e5043e-d12f-4ebd-aa76-f27de0d1bdbb',
        '723ad3be-64b7-4c4e-8086-85ea199c2979',
        '45fc30f6-2682-42eb-8a7b-cc51d8077c48'
    ])
    live_or_on_demand = random.choice(LIVE_OR_ON_DEMAND)
    subscribed_status = random.choice(SUBSCRIBED_STATUS)
    country_code = random.choice(COUNTRIES)
    traffic_source_type = random.choice(TRAFFIC_SOURCE_TYPES)
    traffic_source_detail = random.choice(TRAFFIC_SOURCE_DETAIL)
    views = random.randint(1, 10000)
    watch_time_minutes = round(random.uniform(0.1, 300), 2)
    average_view_duration_seconds = round(random.uniform(1, 600), 2)
    average_view_duration_percentage = round(random.uniform(0, 1), 6)
    red_views = random.randint(0, views)
    red_watch_time_minutes = round(random.uniform(0, watch_time_minutes), 2)
    
    return [date, channel_id, video_id, live_or_on_demand, subscribed_status, country_code,
            traffic_source_type, traffic_source_detail, views, watch_time_minutes,
            average_view_duration_seconds, average_view_duration_percentage, red_views, red_watch_time_minutes]


with open(FILENAME, 'w', newline='') as csvfile:
    fieldnames = ['date', 'channel_id', 'video_id', 'live_or_on_demand', 'subscribed_status', 'country_code',
                  'traffic_source_type', 'traffic_source_detail', 'views', 'watch_time_minutes',
                  'average_view_duration_seconds', 'average_view_duration_percentage', 'red_views',
                  'red_watch_time_minutes']
    
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    
    for _ in range(NUM_ROWS):
        writer.writerow(generate_row())

print(f"{FILENAME} with {NUM_ROWS} rows has been created.")
