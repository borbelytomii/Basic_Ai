import speech_recognition as sr
import requests
import datetime
import sys
import os
from gtts import gTTS
from playsound import playsound
from pprint import pprint
from os.path import dirname, abspath
d = dirname((dirname(abspath(__file__))))
sys.path.append(d)
import config as api
api.API_KEY
err="Say that again sir"
def take_commands():
    # Making the use of Recognizer and Microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            # for listening the command in  english
            query = r.recognize_google(audio, language='en-US')
            # for printing the query or the command that we give
            print("The Inline query is printed'", query, "'")
        except Exception as e:
            print(e)
            speak(err)
            return "None"
    return query
# speak engine
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'sounds/voice.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
# startup sound
def startup():
    startup = 'sounds/startup.mp3'
    playsound(startup)
def tell_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
def work_time():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        if day_of_the_week == 'Monday':
            speak('Your weekend is over. Go to work.')
        elif day_of_the_week == 'Sunday' or day_of_the_week == 'Saturday':
            speak('Today is off.')
        else:
            speak('Go to work.')
def tell_time():
    hour = str(datetime.datetime.today().hour)
    minutes = str(datetime.datetime.today().minute)
    timestamp="It's: "+hour+": "+minutes
    greetings=""
    time = datetime.datetime.now().hour
    # print(time)
    day_time = {1: 'Morning', 2: 'Noon',
                3: 'Afternoon', 4: 'Evening', 5: 'Night'}
    if time < 12 and time >= 5:
        print(day_time[1])
        greetings="Good" + day_time[1]+"Sir"
    if time == 12:
        print(day_time[2])
        greetings="Good" + day_time[2]+"Sir"
    if time > 12 and time <= 17:
        print(day_time[3])
        greetings="Good" + day_time[3]+"Sir"
    if time > 17 and time <= 21:
        print(day_time[4])
        greetings="Good" + day_time[4]+"Sir"
    if time > 21 and time <= 4:
        print(day_time[5])
        greetings="Good" + day_time[5]+"Sir"
    speak(greetings)
    print(timestamp)
    speak(timestamp)
def tell_city():
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
            # and so that assistant can ask for tell_ing
            # again the command
            print(e)
            speak(err)
            return "None"
    return city_name
def tell_weather(speak):
    if speak:
        city = tell_city()
    else:
        city= "Veszprem"
       # Url address with api key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api.API_KEY}&units=metric'
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']
    # Callouts
    speak('Temperature : {} degree celcius'.format(temp))
    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    speak('Description : {}'.format(description))
    print('Description : {}'.format(description))
def tell_commands():
    # City name
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing.. ")
            voice_command = r.recognize_google(audio, language='en-US')
            # for printing the name of the city
            print("The command'", voice_command, "'")
        except Exception as e:
            print(e)
            speak(err)
            return "None"
    return voice_command
# Driver Code
if __name__ == '__main__':
    startup()
    speak("How Can I help you today Sir?")
    while tell_commands() != 'over':
        command = take_commands()
        if "morning" in command:
            tell_day()
            tell_time()
            tell_weather(False)
            work_time()
        if "day" in command:
            tell_day()
            tell_time()
        if "weather" in command:
            # tell_City()
            tell_weather(True)
