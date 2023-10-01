import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# The number of rows of data to generate
num_rows = random.randint(4332,7648)

# Open a CSV file in write mode
with open('p_channel_basic_a2_channel.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    
    # Write the header row
    writer.writerow([
        'date', 'channel_id', 'video_id', 'live_or_on_demand', 'subscribed_status', 'country_code', 
        'views', 'comments', 'likes', 'dislikes', 'shares', 'watch_time_minutes', 'average_view_duration_seconds', 
        'average_view_duration_percentage', 'annotation_impressions', 'annotation_clickable_impressions', 'annotation_clicks', 
        'annotation_click_through_rate', 'annotation_closable_impressions', 'annotation_closes', 'annotation_close_rate', 
        'card_teaser_impressions', 'card_teaser_clicks', 'card_teaser_click_rate', 'card_impressions', 'card_clicks', 
        'card_click_rate', 'subscribers_gained', 'subscribers_lost', 'videos_added_to_playlists', 'videos_removed_from_playlists', 
        'red_views', 'red_watch_time_minutes'
    ])
    
    # Generate and write the data rows
    for _ in range(num_rows):
        writer.writerow([
            (datetime.now() - timedelta(days=random.randint(0, 7))).strftime('%Y%m%d'),  # date
            "b3aae0c1-8e21-4100-9def-5093d454022f",  # channel_id
            random.choice([
                'cae7a02f-b2b3-4619-ad4d-620f470a7182',
                'a5ce5123-bc8f-432f-af10-5b7046808e77',
                'a5e5043e-d12f-4ebd-aa76-f27de0d1bdbb',
                '723ad3be-64b7-4c4e-8086-85ea199c2979',
                '45fc30f6-2682-42eb-8a7b-cc51d8077c48'
            ]),  # video_id
            random.choice(['live', 'on_demand']),  # live_or_on_demand
            random.choice(['subscribed', 'not_subscribed']),  # subscribed_status
            fake.country_code() if random.randint(0, 1) == 0 else "US",  # country_code
            random.randint(0, 10000),  # views
            random.randint(0, 500),  # comments
            random.randint(0, 1000),  # likes
            random.randint(0, 1000),  # dislikes
            random.randint(0, 500),  # shares
            random.uniform(0, 10000),  # watch_time_minutes
            random.uniform(0, 3000),  # average_view_duration_seconds
            round(random.uniform(0, 1), 6),  # average_view_duration_percentage
            random.randint(0, 1000),  # annotation_impressions
            random.randint(0, 500),  # annotation_clickable_impressions
            random.randint(0, 250),  # annotation_clicks
            random.uniform(0, 1),  # annotation_click_through_rate
            random.randint(0, 500),  # annotation_closable_impressions
            random.randint(0, 250),  # annotation_closes
            random.uniform(0, 1),  # annotation_close_rate
            random.randint(0, 1000),  # card_teaser_impressions
            random.randint(0, 500),  # card_teaser_clicks
            random.uniform(0, 1),  # card_teaser_click_rate
            random.randint(0, 1000),  # card_impressions
            random.randint(0, 500),  # card_clicks
            random.uniform(0, 1),  # card_click_rate
            random.randint(0, 1000),  # subscribers_gained
            random.randint(0, 500),  # subscribers_lost
            random.randint(0, 1000),  # videos_added_to_playlists
            random.randint(0, 500),  # videos_removed_from_playlists
            random.randint(0, 1000),  # red_views
            random.uniform(0, 10000)  # red_watch_time_minutes
        ])
        
print(f"{num_rows} rows of data have been written to youtube_data.csv")
