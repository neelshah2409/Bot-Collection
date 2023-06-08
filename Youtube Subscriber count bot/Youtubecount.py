# code for Youtube Subscriber count bot

import os
import time
import googleapiclient.discovery
from google.oauth2 import service_account

# Set up credentials
credentials_file = 'credentials.json'  # Replace with your credentials file path
credentials = service_account.Credentials.from_service_account_file(credentials_file)
api_service_name = 'youtube'
api_version = 'v3'
client = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

# YouTube channel ID of the channel you want to monitor
channel_id = 'CHANNEL_ID'  # Replace with the desired YouTube channel ID

# Trigger value for notification
trigger_value = 500  # Replace with your desired trigger value

# Function to get the subscriber count of the specified channel
def get_subscriber_count(channel_id):
    request = client.channels().list(part='statistics', id=channel_id)
    response = request.execute()
    subscriber_count = int(response['items'][0]['statistics']['subscriberCount'])
    return subscriber_count

# Continuous display
def continuous_display():
    while True:
        subscriber_count = get_subscriber_count(channel_id)
        print(f"Subscriber count: {subscriber_count}")
        time.sleep(60)  # Delay between each check (in seconds)

# Notification function
def check_trigger_value():
    while True:
        subscriber_count = get_subscriber_count(channel_id)
        print(f"Subscriber count: {subscriber_count}")
        if subscriber_count > trigger_value:
            print("Subscriber count has crossed the trigger value!")
            # Add your notification logic here
            break
        time.sleep(60)  # Delay between each check (in seconds)

# Uncomment one of the following lines to choose the desired mode

# Continuous display mode
# continuous_display()

# Notification mode
# check_trigger_value()
