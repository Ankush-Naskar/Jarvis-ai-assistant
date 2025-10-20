from gtts import gTTS
import pygame
import os


def speak(text):
    tts = gTTS(text)
    tts.save('audio.mp3')

    # Initialize mixer and pygame
    pygame.mixer.pre_init(24000, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
     # Load and play MP3
    pygame.mixer.music.load("audio.mp3") 
    pygame.mixer.music.play()
    # Keep script alive while music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("audio.mp3")