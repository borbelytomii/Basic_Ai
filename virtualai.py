#import modules

import config as api
import datetime
import pyttsx3
import speech_recognition as sr
import requests
from pprint import pprint

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


def Speak(audio):

    # intial constructor of pyttsx3
    engine = pyttsx3.init()

    # getter and setter method
    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
    engine.say(audio)
    engine.runAndWait()


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


def tellHour():

    time = datetime.datetime.now().hour
    print(time)

    day_time = {1: 'Morning', 2: 'Noon',
                3: 'Afternoon', 4: 'Evening', 5: 'Night'}

    if time < 12 and time >= 5:
        print(day_time[1])
        Speak("Good" + day_time[1]+"Sir")

    if time == 12:
        print(day_time[2])
        Speak("Good" + day_time[2]+"Sir")

    if time > 12 and time <= 17:
        print(day_time[3])
        Speak("Good" + day_time[3]+"Sir")

    if time > 17 and time <= 21:
        print(day_time[4])
        Speak("Good" + day_time[4]+"Sir")

    if time > 21 and time <= 4:
        print(day_time[5])
        Speak("Good" + day_time[5]+"Sir")


def tellCity():
    #City name
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
    city  = tellCity()
    #Url address with api key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api.API_KEY}&units=metric'

    res = requests.get(url)

    data = res.json()

    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']

    #Callouts
    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))


# Driver Code
if __name__ == '__main__':
    command = take_commands()

    if "day" in command:
        tellDay()
        tellHour()
    if "weather" in command:
        tellCity()
        tellWeather()
