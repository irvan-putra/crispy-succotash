# based on this: https://medium.com/@dominique.heer/controlling-your-computer-with-voice-commands-by-using-openai-whisper-09c867c635b2

import time
import speech_recognition as sr
import pyautogui

screen_width , screen_height = pyautogui.size()

def callback(recognizer: sr.Recognizer, audio):
    print("::listening::")
    try:
        recog: str = recognizer.recognize_whisper(audio, language="english", model="base")
        print("::whisper recognized:: " + recog) # for debugging
        text = recog.lower().strip()
        if text.startswith("next"):
            pyautogui.click()
        elif text.startswith("back"):
            pyautogui.press('left')
    except sr.UnknownValueError:
        print("::could not understand audio::")
    except sr.RequestError as e:
        print("::an error occurred:: {0}".format(e))
    print("::sleeping::")


r = sr.Recognizer()
m = sr.Microphone()

time.sleep(5)
print("::adjusting for ambient noise, please be silent::")
time.sleep(5)
with m as source:
    r.adjust_for_ambient_noise(source, duration=1.0)
time.sleep(5)
print("::adjusting for ambient noise done, thanks::")
time.sleep(5)

stop_listening = r.listen_in_background(m, callback)

for _ in range(600):
    time.sleep(1)

stop_listening(wait_for_stop=True)
