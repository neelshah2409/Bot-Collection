# Python Instragram Follower count bot

from instagram_private_api import Client, ClientCompatPatch

# Instagram username and password
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

# Function to get the follower count of the specified Instagram account
def get_follower_count(username):
    api = Client(username, password)
    user_info = api.username_info(username)
    follower_count = user_info['user']['follower_count']
    return follower_count

# Continuous display
def continuous_display():
    while True:
        follower_count = get_follower_count(username)
        print(f"Follower count: {follower_count}")
        time.sleep(60)  # Delay between each check (in seconds)

# Notification function
def check_trigger_value():
    while True:
        follower_count = get_follower_count(username)
        print(f"Follower count: {follower_count}")
        if follower_count > trigger_value:
            print("Follower count has crossed the trigger value!")
            # Add your notification logic here
            break
        time.sleep(60)  # Delay between each check (in seconds)

# Uncomment one of the following lines to choose the desired mode

# Continuous display mode
# continuous_display()

# Notification mode
# check_trigger_value()
