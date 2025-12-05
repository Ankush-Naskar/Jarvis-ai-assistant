import os
import json

def create_user_info():
    if not os.path.exists("user_settings.py"):
        data = '''
# 🔐 API Keys (only include what you actually use)
OPENAI_API_KEY = "<Enter your open ai api key>"

# 📍 Location Settings
LOCATION_FOR_WEATHER = "kolkata"

# 🕒 Timeout Settings
DURATION_OF_TIMEOUT = 60 # Durationn should be in second
    '''

        with open("user_settings.py", "w", encoding="utf-8") as f:
            f.write(data)
# create_user_info()



def json_handling():
    with open("data_source/config.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
    return json_data

config_data = json_handling() 


def youtube_videos(name): 

    video_links = config_data["videos"].get(name)
    return(video_links)


def link_open(name):
    links = config_data["links"].get(name)
    return(links)

