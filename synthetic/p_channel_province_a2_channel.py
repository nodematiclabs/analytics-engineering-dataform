import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Number of rows to generate
num_rows = random.randint(800,1000)

fieldnames = [
    "date", "channel_id", "video_id", "live_or_on_demand", "subscribed_status",
    "country_code", "province_code", "views", "watch_time_minutes",
    "average_view_duration_seconds", "average_view_duration_percentage",
    "annotation_click_through_rate", "annotation_close_rate", "annotation_impressions",
    "annotation_clickable_impressions", "annotation_closable_impressions", "annotation_clicks",
    "annotation_closes", "card_click_rate", "card_teaser_click_rate", "card_impressions",
    "card_teaser_impressions", "card_clicks", "card_teaser_clicks", "red_views", "red_watch_time_minutes"
]

with open('p_channel_province_a2_channel.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    for _ in range(num_rows):
        row = {
            "date": (datetime.now() - timedelta(days=random.randint(0, 7))).strftime('%Y%m%d'),
            "channel_id": "b3aae0c1-8e21-4100-9def-5093d454022f",
            "video_id": random.choice([
                'cae7a02f-b2b3-4619-ad4d-620f470a7182',
                'a5ce5123-bc8f-432f-af10-5b7046808e77',
                'a5e5043e-d12f-4ebd-aa76-f27de0d1bdbb',
                '723ad3be-64b7-4c4e-8086-85ea199c2979',
                '45fc30f6-2682-42eb-8a7b-cc51d8077c48'
            ]),
            "live_or_on_demand": random.choice(["live", "on_demand"]),
            "subscribed_status": random.choice(["subscribed", "not_subscribed"]),
            "country_code": "US",
            "province_code": "US-" + fake.state_abbr(),
            "views": random.randint(1, 10000),
            "watch_time_minutes": round(random.uniform(0.1, 1000), 6),
            "average_view_duration_seconds": round(random.uniform(1, 1000), 6),
            "average_view_duration_percentage": round(random.uniform(0, 1), 6),
            "annotation_click_through_rate": round(random.uniform(0, 1), 6),
            "annotation_close_rate": round(random.uniform(0, 1), 6),
            "annotation_impressions": random.randint(0, 1000),
            "annotation_clickable_impressions": random.randint(0, 1000),
            "annotation_closable_impressions": random.randint(0, 1000),
            "annotation_clicks": random.randint(0, 1000),
            "annotation_closes": random.randint(0, 1000),
            "card_click_rate": round(random.uniform(0, 1), 6),
            "card_teaser_click_rate": round(random.uniform(0, 1), 6),
            "card_impressions": random.randint(0, 1000),
            "card_teaser_impressions": random.randint(0, 1000),
            "card_clicks": random.randint(0, 1000),
            "card_teaser_clicks": random.randint(0, 1000),
            "red_views": random.randint(0, 1000),
            "red_watch_time_minutes": round(random.uniform(0, 1000), 6)
        }
        
        writer.writerow(row)
