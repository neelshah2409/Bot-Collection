import os
import googleapiclient.discovery
import youtube_dl
import json

# Set up the YouTube Data API client
api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyBswgNj2nKUeVKp7MRHT0Fz7RvGTpMReIA"  # Replace with your actual API key
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)


def search_videos(query):
    # Search for videos based on the user's query
    request = youtube.search().list(
        part="snippet",
        maxResults=7,  # Adjust the number of results as needed
        q=query
    )
    response = request.execute()

    # Extract the video details from the search results
    videos = []
    for item in response['items']:
        if item['id'].get('videoId'):
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            videos.append({'video_id': video_id, 'title': title, 'description': description})

    return videos


def show_video_details(video_id):
    # Retrieve additional details for a specific video
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()

    # Extract the likes and tags from the video details
    video = response['items'][0]
    likes = video['statistics']['likeCount']
    channel = video['snippet']['channelTitle']

    return likes, channel


def download_video(video_id):
    # Download the video using youtube-dl
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Adjust the download directory as needed
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={video_id}'])


# Main program loop
while True:
    query = input("Enter your search query (q to quit): ")
    if query.lower() == "q":
        break

    videos = search_videos(query)

    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']} - {video['description']}")

    video_number = input("Enter the number of the video you want to watch (0 to cancel): ")
    if video_number == "0":
        continue

    selected_video = videos[int(video_number) - 1]
    video_id = selected_video['video_id']
    likes, channel = show_video_details(video_id)

    print(f"Likes: {likes}")
    print(f"Channel Name: {', '.join(channel)}")

    download_choice = input("Do you want to download this video? (y/n): ")
    if download_choice.lower() == "y":
        download_video(video_id)

    print("")

