import speech_recognition as sr
import webbrowser
import time
import asyncio
from datetime import datetime, timedelta
from data_source import music_library, URLs, openAi
from jarvis_system.speak_system import speak
from jarvis_system import notification_system
from data_source.Weather import get_current_weather, get_weather_by_date
import User_info

# Guide
print("say 'jarvis' to start"
        " and 'stop program' to stop jarvis\n")



# Processes voice commands
def processCommand(c):
    # speak(c)

    # Opening links.
    if c.lower().startswith("open"):
        search = " ".join(c.lower().split(" ")[1:])
        link_ = URLs.links.get(search)
        if link_:
            speak(f"opening {search}")
            webbrowser.open(link_)
        else:
            speak(f"{search} is not Predefined. Searching in google")
            query = search.replace(" ", "+")
            link_ = f"https://www.google.com/search?q={query}"
            webbrowser.open(link_)
        

    # Google search.
    elif c.lower().startswith("search"):
        search = " ".join(c.lower().split(" ")[1:])
        speak(f"Searching {search} in google")
        query = search.replace(" ", "+")
        link_ = f"https://www.google.com/search?q={query}"
        webbrowser.open(link_) 
        

    # Playing songs
    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split(" ")[1:])
        link_ = music_library.music.get(song)
        if link_:
            speak(f"Playing {song}")
            webbrowser.open(link_)
        else:
            speak(f"Playing {song} from YouTube")
            query = song.replace(" ", "+")
            song_link = f"https://www.google.com/search?q={query}+site:youtube.com&btnI"
            webbrowser.open(song_link)

    # Weather updates
    
    elif "weather update" in c.lower():
        Location = User_info.LOCATION_FOR_WEATHER
        
        if "current" in c.lower():
            l = asyncio.run(get_current_weather())
            speak(l)
        elif "today" in c.lower():
            today = datetime.today().date()
            l = asyncio.run(get_weather_by_date(Location, today))
            speak("today," + l)
        elif "tomorrow" in c.lower():
            tomorrow = (datetime.today().date() + timedelta(days=1))
            l = asyncio.run(get_weather_by_date(Location, tomorrow))
            speak("tomorrow," + l)
        else:
            l = asyncio.run(get_current_weather())
            speak(l)


    # Ai integration --OpenAi
    # else:
    #     speak(openAi.AI(c))


            
if __name__ == "__main__":
    speak("Initializing jarvis......")
   
    # Notification  system
    notification_system.notify_start()

    # Time Checking --- notification 
    last_active = time.time()
    timeout_duration = User_info.DURATION_OF_TIMEOUT # time in second


    while True:
        print("Recognizing.....")

        # Closing notification --- time limit
        if time.time() - last_active > timeout_duration:
            notification_system.notify_timeout()
            break


        try:
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

                # Wake up command
                word = r.recognize_google(audio)
                if word.lower() in ["hello", "jarvis", "hello jarvis"]:
                    speak("Yes, how can i help you?")
                    print("jarvis active...")
                    last_active = time.time() # Time-limit system


                    # Google Speech recognition
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

                # Closing Jarvis
                elif word.lower() in ["stop program", "stop jarvis"]:
                    speak("closing jarvis")
                    print("closing jarvis.....")
                    
                    # Notification system
                    notification_system.notify_stop()
                    break


        except Exception as e:
            print("error; {0}".format(e))
            print("")
            # Guide
            print("say 'jarvis' to start"
                " and 'stop program' to stop jarvis\n")
