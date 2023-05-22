import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main1():
    # Disable OAuthlib's HTTPS verification when running locally.
    # DO NOT leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secret.json"

    # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes)
    # credentials = flow.run_local_server(port=8080)
    # youtube = googleapiclient.discovery.build(
    #     api_service_name, api_version, credentials=credentials)

    # request = youtube.search().list(
    #     part="snippet",
    #     channelType="any",
    #     maxResults=15,
    #     order="relevance",
    #     q="javascript"
    # )
    # response = request.execute()

     #JsonResponseReader()

def main():
    # f = open('demo.json')
    # data = json.load(f)
    # for i in data['haschilde']:
    #  print(i['iftrue'])
    #
    # f.close()
    jsonFileReader()

def jsonFileReader():
        with open('demo.json', 'r') as f:
            data = json.load(f)
        title = data['items'][0]['snippet']['title']
        print(title)


# def jsonFileReader():
#     with open('demo.json', 'r') as f:
#         data = json.load(f)
#         # title = data["items"]["snippet"]
#     # for title in data['items'][0]['snippet']:
#     #     print(title['title'])
#     title = data['items'][0]['snippet']['title']
#     print(title)

        f.close()

# if _name_ == "_main_":
#     main()