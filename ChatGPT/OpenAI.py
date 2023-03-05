import speech_recognition as sr
import pyttsx3
import openai
import os 
from gtts import gTTS
import  vlc
import time

openai.api_key = "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"
p = vlc.MediaPlayer("voice.mp3")
sett = open("settings.txt", "r").readlines()[0][:-1]


while True:
    model_engine = "text-davinci-003"
    prompt = str(input("me: "))
    if prompt[0] != "-":
        p.stop()

        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text
        print("chatGPT: " + response)
        tts = gTTS(text=response, lang=sett)
        tts.save("voice.mp3")
        p = vlc.MediaPlayer("voice.mp3")
        p.play()
    else:
        if prompt[1:] == "en" or prompt[1:] == "fr" or prompt[1:] == "zh-CN" or prompt[1:] == "zh-TW" or prompt[1:] == "pt" or prompt[1:] == "es":
            sett = prompt[1:]
        elif prompt[1:] == "end":
            break
