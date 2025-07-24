# Import the gTTS module for text-to-speech conversion
from gtts import gTTS
# Import the detect function from langdetect to automatically detect the language
from langdetect import detect
import os

with open("sample.txt","r",encoding="utf-8") as file:
    text=file.read()

lang=detect(text)
print(f"Detect language:{lang}")

speech = gTTS(text=text,lang=lang,slow=False)

speech.save("sound.mp3")
os.system(" start sound.mp3") 


