# JARVIS - Voice Assistant (README)

## 📌 INTRODUCTION

Jarvis is a modular, voice-controlled assistant built with Python. It listens for voice commands, responds with speech, and performs tasks such as opening websites, playing music and YouTube videos, and searching Google. While designed to run locally, it utilizes online services like *Google Text-to-Speech* (*gTTS*) for voice output. If the user provides an OpenAI API key, Jarvis can optionally generate intelligent spoken responses using AI.
## 🛠️ HOW IT WORKS

- To activate Jarvis, first say the wake word: *"Jarvis"*.
- Once activated, Jarvis listens for your next voice command.
- If the command starts with *"open"*, it checks a predefined list of websites. If the site is not predefined, it will search for it on Google.
- If the command starts with *"search"*, Jarvis will perform a Google search using your query.
- If the command starts with *"play"*, it first checks a predefined music library. If the song is not predefined, Jarvis will play the top result from a YouTube search. This command can be used to play any YouTube video, not just music.
- If the command includes *"weather update"*, Jarvis will provide a weather report. It can deliver **current**, **today**’s, or **tomorrow**’s weather updates based on your location in `User_info.py`. One of the keywords — *"current"*, *"today"* or *"tomorrow"* — must be included in the command. By default, the location is Kolkata.
- For general questions, Jarvis can use OpenAI to generate intelligent spoken responses (*optional*, requires API key).
- If Jarvis is not activated, you can shut it down by saying *"stop jarvis"*, or it will automatically shut down after a period of inactivity (Default: *60 seconds*), as defined in the `DURATION_OF_TIMEOUT` setting in `User_info.py`.

## 🔧 SETUP INSTRUCTIONS
Before running jarvis, open `User_info.py` and update the following fields:
- `OPENAI_API_KEY` = "Enter your OpenAI API key" (*optional*)
- `LOCATION_FOR_WEATHER` = "Enter your location for weather updates"
- `DURATION_OF_TIMEOUT` = "Enter timeout duration in seconds"

You can ignore  `OPENAI_API_KEY` if you don’t want to enable the AI feature.

## 📢 VOICE COMMANDS

To start Jarvis, say                                  ➔ *"jarvis"*

Once activated,
- To open predefined sites    ➔  "*open* [website]"
- To perform a Google search   ➔  "*search* [query]"
- To play YouTube music or video  ➔  "*play* [song_or_video]"
- For weather report                                      ➔  "["*current*"/"*today*"/"*tomorrow*"] *weather update*"

To stop Jarvis, say    ➔ *"stop jarvis"*

## ✨ FEATURES
1. 🔗 Website Launcher

   Say "open" followed by any of these:
   - google → https://google.com
   - YouTube → https://youtube.com
   - github → https://github.com
   - chatgpt → https://chat.openai.com
   - Code With Harry → https://www.codewithharry.com
   - Claude_ai → https://claude.ai
   - flipkart → https://flipkart.com
   - hackerrank → https://hackerrank.com

    You can add more predefined sites by editing the  *"data_source/URLs.py"* file.

2. 🎵 Music Player

   Say "play" followed by any of these:
   - despacito → https://www.youtube.com/watch?v=kJQP7kiw5Fk
   - shape of you → https://www.youtube.com/watch?v=JGwWNGJdvx8
   - believer → https://www.youtube.com/watch?v=7wtfhZwyrcc

   You can add more predefined songs even videos by editing the  *"data_source/music_library.py"* file.

3. 🌦️ Weather Forecast  

   Get detailed weather updates by saying something like:  
   - *"What is the current weather update?"* → Live temperature, wind, visibility, and pressure  
   - *"What is the weather update for today?"* → Forecast with average wind speed, atmospheric pressure, and day-type summary that includes intelligent warnings like rain, thunderstorms, fog, or windy conditions.  
   - *"What is the weather update for tomorrow?"* → Same as above

4. 🧠 AI Assistant (*Optional*)

   For general queries like *"what is coding"* or *"who is the prime minister"*, Jarvis can use OpenAI to generate intelligent spoken responses. If you have an OpenAI API key, you can enable this feature by uncommenting the OpenAI-related lines in `main.py` (around line 80-81). By default, this feature is commented out to avoid token-based dependencies. You’ll also need to add your API key to the `OPENAI_API_KEY` from `User_info.py`

5. 🔔 Notifications

   Jarvis shows desktop notifications when it **starts**, **stops**, or **times out** due to inactivity.

6. 🕒 Auto Shutdown

   Jarvis automatically shuts down after a period of inactivity, based on the timeout duration set in `User_info.py` (default: *60 seconds*), to save system resources.


## 📁 FILE & FOLDER STRUCTURE

![File-Structure](image.png)

## 🧑‍💻 USER CONFIGURATION

Jarvis uses a centralized configuration file called `User_info.py` to store user-specific settings. This keeps your system modular and makes it easy to personalize or extend.

What goes inside `User_info.py`:
- `OPENAI_API_KEY` → *Optional*. Used only if you enable AI responses.
- `LOCATION_FOR_WEATHER` →  Location used for weather updates. (default: *"Kolkata"*)
- `DURATION_OF_TIMEOUT` → Time (in seconds) before Jarvis shuts down due to inactivity. (default: *60*)



## 🔒 PRIVACY NOTICE

Jarvis is designed to run entirely on your local machine. No voice data, commands, or personal information are stored or transmitted to external servers unless explicitly enabled by the user.

- By default, all features operate offline using local Python modules.
- Only services like *Google Text-to-Speech* (*gTTS*), *python-weather* and *OpenAI*(*optional*) are online.
- When OpenAI integration is enabled, prompts are sent to *OpenAI*'s servers for processing. No data is stored locally or reused beyond the current session.
- Jarvis does not log, save, or share any voice recordings, transcripts, or user activity.
- You remain in full control of your data.

This privacy-first design ensures Jarvis remains lightweight, secure, and respectful of your personal environment.


## 📦 INSTALLATION

1. Install dependencies:
   - pip install -r requirements.txt

2. Run Jarvis:
   - main.py

## 🧩 IMPORTED MODULES  
- `speech_recognition` → for capturing and recognizing voice input  
- `webbrowser` → to open websites and YouTube links  
- `time` → for tracking inactivity and triggering auto-shutdown  
- `asyncio` → to run asynchronous weather functions  
- `datetime`, `timedelta` → for handling date-based weather queries  
- `dateutil.parser` → to parse natural language dates (optional use)  
- `data_source.music_library` → predefined song links  
- `data_source.URLs` → predefined website links  
- `data_source.Weather` → weather functions: `get_current_weather()`, `get_weather_by_date()`  
- `jarvis_system.speak_system` → `speak()` function for voice output  
- `jarvis_system.notification_system` → desktop notifications: `notify_start()`, `notify_stop()`, `notify_timeout()`

🗓️ Last updated: 21 October 2025