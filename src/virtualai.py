import speech_recognition as sr
import requests
import datetime
import sys
import os
from winsound import PlaySound
from gtts import gTTS
from playsound import playsound
from pprint import pprint
from os.path import dirname, abspath
d = dirname((dirname(abspath(__file__))))
sys.path.append(d)
import config as api
# API_KEY='' in config.py
api.API_KEY


def take_commands():

    # Making the use of Recognizer and Microphone
    # Method from Speech Recognition for taking
    # commands
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")

            # for listening the command in  english
            Query = r.recognize_google(audio, language='en-US')

            # for printing the query or the command that we give
            print("The Inline query is printed'", Query, "'")
        except Exception as e:

            # this method is for handling the exception
            # and so that assistant can ask for telling
            # again the command
            print(e)
            Speak("Say that again sir")
            return "None"

    return Query

# Speak engine


def Speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'sounds/voice.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# Startup sound


def Startup():
    startup = 'sounds/startup.mp3'
    playsound(startup)


def tellDay():

    # the weekday method is a method from datetime
    # library which helps us to an integer
    # corresponding to the day of the week
    # this dictionary will help us to map the
    # integer with the day and we will check for
    # the condition and if the condition is true
    # it will return the day
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        Speak("The day is " + day_of_the_week)


def Worktime():

    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        #todays_day = day_of_the_week
        #Speak("The day is " + day_of_the_week)

        if day_of_the_week == 'Monday':
            Speak('Your weekend is over. Go to work.')
        elif day_of_the_week == 'Sunday' or day_of_the_week == 'Saturday':
            Speak('Today is off.')
        else:
            Speak('Go to work.')


def tellTime():

    hour = str(datetime.datetime.today().hour)
    minutes = str(datetime.datetime.today().minute)

    time = datetime.datetime.now().hour
    # print(time)

    day_time = {1: 'Morning', 2: 'Noon',
                3: 'Afternoon', 4: 'Evening', 5: 'Night'}

    if time < 12 and time >= 5:
        print(day_time[1])
        Speak("Good" + day_time[1]+"Sir")
        print("It's: "+hour+": "+minutes)
        Speak("It's: "+hour+": "+minutes)

    if time == 12:
        print(day_time[2])
        Speak("Good" + day_time[2]+"Sir")
        print("It's: "+hour+": "+minutes)
        Speak("It's: "+hour+": "+minutes)

    if time > 12 and time <= 17:
        print(day_time[3])
        Speak("Good" + day_time[3]+"Sir")
        print("It's: "+hour+": "+minutes)
        Speak("It's: "+hour+": "+minutes)

    if time > 17 and time <= 21:
        print(day_time[4])
        Speak("Good" + day_time[4]+"Sir")
        print("It's: "+hour+": "+minutes)
        Speak("It's: "+hour+": "+minutes)

    if time > 21 and time <= 4:
        print(day_time[5])
        Speak("Good" + day_time[5]+"Sir")
        print("It's: "+hour+": "+minutes)
        Speak("It's: "+hour+": "+minutes)


def tellCity():
    # City name
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing City name")

            city_name = r.recognize_google(audio, language='en-US')

            # for printing the name of the city
            print("The name of the City'", city_name, "'")
        except Exception as e:

            # this method is for handling the exception
            # and so that assistant can ask for telling
            # again the command
            print(e)
            Speak("Say that again sir")
            return "None"

    return city_name


def tellWeather():
    #city = input('Enter your city : ')
    city = tellCity()
    # Url address with api key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api.API_KEY}&units=metric'

    res = requests.get(url)

    data = res.json()

    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']

    # Callouts
    Speak('Temperature : {} degree celcius'.format(temp))
    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    Speak('Description : {}'.format(description))
    print('Description : {}'.format(description))


def defaultWeather():
    city = "Veszprem"
    # Url address with api key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api.API_KEY}&units=metric'

    res = requests.get(url)

    data = res.json()

    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']

    # Callouts
    Speak('Temperature : {} degree celcius'.format(temp))
    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    Speak('Description : {}'.format(description))
    print('Description : {}'.format(description))


def tellCommands():
    # City name
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing.. ")

            voice_command = r.recognize_google(audio, language='en-US')

            # for printing the name of the city
            print("The command'", voice_command, "'")
        except Exception as e:

            # this method is for handling the exception
            # and so that assistant can ask for telling
            # again the command
            print(e)
            Speak("Say that again sir")
            return "None"

    return voice_command


# Driver Code
if __name__ == '__main__':
    Startup()
    Speak("How Can I help you today Sir?")
    while tellCommands() != 'over':
        command = take_commands()
        if "morning" in command:
            tellDay()
            tellTime()
            defaultWeather()
            Worktime()

        if "day" in command:
            tellDay()
            tellTime()

        if "weather" in command:
            # tellCity()
            tellWeather()
