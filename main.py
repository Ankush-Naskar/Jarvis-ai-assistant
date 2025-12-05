import speech_recognition as sr
import time
from jarvis_modules.file_handling import create_user_info
create_user_info()
from jarvis_modules import notification_system, command_handling

from jarvis_modules.speak_system import speak
from data_source import openAi
import user_settings

# Guide
print("say 'jarvis' to start"
        " and 'stop program' to stop jarvis\n")


# Processes voice commands
def processCommand(c):

    # Opening links.
    if c.lower().startswith("open"):
        command_handling.open_links(c)

    # Google search.
    elif c.lower().startswith("search"):
        command_handling.google_search(c)

    # Playing songs
    elif c.lower().startswith("play"):
        command_handling.play_YT_song_video(c)

    # Weather updates
    elif "weather update" in c.lower():
        command_handling.weather_update(c)

    # Ai integration --OpenAi
    else:
        speak(openAi.AI(c))


            
if __name__ == "__main__":
    speak("Initializing jarvis......")
   
    # Notification  system
    notification_system.notify_start()

    # Time Checking --- notification 
    last_active = time.time()
    timeout_duration = user_settings.DURATION_OF_TIMEOUT # time in second


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
                if word.lower() in ["jarvis", "hello jarvis"]:
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
                " and 'stop jarvis' to stop jarvis\n")
