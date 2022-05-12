from nltk.sentiment import SentimentIntensityAnalyzer
from numpy import positive
import pyttsx3
import speech_recognition as sr
sia = SentimentIntensityAnalyzer()
dict = sia.polarity_scores("positive.txt")
print(dict)
p = open("positive.txt", 'r')
li = p.read()
engine = pyttsx3.init(driverName="sapi5")
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('voice', voices[1].id)
# changing the rate of the voice
engine.setProperty("rate", 150)
engine.setProperty('volume', volume-0.001)
print("positive")
engine.say('<pitch absmiddle="10">{li}</pitch>')
engine.runAndWait()
# def say_something():

#     r5 = sr.Recognizer()
#     with sr.Microphone() as source:

#         engine = pyttsx3.init(driverName="sapi5")
#         engine.runAndWait()

#         audio = r5.listen(source)
#         audio = r5.recognize_google(audio)
#         dict = sia.polarity_scores(audio)
#         print(audio)
#         print(dict)
#         if dict.get('pos') > dict.get('neg') and dict.get('pos') > dict.get('neu'):
#             engine = pyttsx3.init(driverName="sapi5")
#             voices = engine.getProperty('voices')
#             volume = engine.getProperty('volume')
#             engine.setProperty('voice', voices[1].id)
#             engine.setProperty("rate", 200)  # changing the rate of the voice
#             engine.setProperty('volume', volume-0.001)
#             print("positive")
#             engine.say(audio)
#             engine.runAndWait()

#         elif dict.get('neu') > dict.get('neg') and dict.get('neu') > dict.get('pos'):
#             engine = pyttsx3.init(driverName="sapi5")
#             voices = engine.getProperty('voices')
#             volume = engine.getProperty('volume')
#             engine.setProperty('voice', voices[1].id)
#             engine.setProperty("rate", 150)  # changing the rate of the voice
#             engine.setProperty('volume', volume-0.001)
#             print("neutral")
#             engine.say(audio)
#             engine.runAndWait()
#         else:
#             engine = pyttsx3.init(driverName="sapi5")
#             voices = engine.getProperty('voices')
#             volume = engine.getProperty('volume')
#             engine.setProperty('voice', voices[1].id)  # changing the voice
#             engine.setProperty("rate", 130)  # changing the rate of the voice
#             engine.setProperty('volume', volume-0.001)
#             engine.say(audio)
#             engine.say(
#                 '<pitch absmiddle="5"> This text should be spoken at pitch five. <pitch absmiddle="-5"> This text should be spoken at pitch negative five. </pitch> </pitch> <pitch absmiddle="10"/> ')
#             engine.runAndWait()

# say_something()
