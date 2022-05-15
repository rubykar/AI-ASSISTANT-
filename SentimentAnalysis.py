from nltk.sentiment import SentimentIntensityAnalyzer
import pyttsx3
import speech_recognition as sr
sia = SentimentIntensityAnalyzer()
p = open("kavi.txt", 'r')
li = p.read()
dict = sia.polarity_scores(li)
new = li.split()
print(new)
dor1 = '<pitch absmiddle="10">'+li+'</pitch>'
dor2 = '<pitch absmiddle="4">'+li+'</pitch>'
dor3 = '<pitch absmiddle="6">'+li+'</pitch>'
print(dict)
# engine = pyttsx3.init(driverName="sapi5")
# voices = engine.getProperty('voices')
# volume = engine.getProperty('volume')
# engine.setProperty('voice', voices[1].id)
# # changing the rate of the voice
# engine.setProperty("rate", 200)
# engine.setProperty('volume', volume-0.001)
# engine.say(says)good
# engine.say(dor)
# # engine.say('<pitch absmiddle="5">My day was pretty good ,what about you?</pitch>')
# # engine.say('<pitch absmiddle="10">My day was pretty bad ,what about you?</pitch>')
# engine.runAndWait()


def say_something():
    r5 = sr.Recognizer()
    with sr.Microphone() as source:
        engine = pyttsx3.init(driverName="sapi5")
        engine.runAndWait()
        # audio = r5.listen(source)
        # audio = r5.recognize_google(audio)
        # dict = sia.polarity_scores(audio)
        # print(audio)
        # print(dict)
        if dict.get('pos') > dict.get('neg') and dict.get('pos') > dict.get('neu'):
            engine = pyttsx3.init(driverName="sapi5")
            voices = engine.getProperty('voices')
            volume = engine.getProperty('volume')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty("rate", 180)  # changing the rate of the voice
            engine.setProperty('volume', volume-0.001)
            print("positive")
            engine.say(dor1)
            engine.runAndWait()
        elif dict.get('neu') > dict.get('neg') and dict.get('neu') > dict.get('pos'):
            engine = pyttsx3.init(driverName="sapi5")
            voices = engine.getProperty('voices')
            volume = engine.getProperty('volume')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty("rate", 160)  # changing the rate of the voice
            engine.setProperty('volume', volume-0.001)
            print("neutral")
            engine.say(dor3)
            engine.runAndWait()
        else:
            engine = pyttsx3.init(driverName="sapi5")
            voices = engine.getProperty('voices')
            volume = engine.getProperty('volume')
            engine.setProperty('voice', voices[1].id)  # changing the voice
            engine.setProperty("rate", 130)  # changing the rate of the voice
            engine.setProperty('volume', volume-0.001)
            engine.say(
                dor2)
            engine.runAndWait()


say_something()
