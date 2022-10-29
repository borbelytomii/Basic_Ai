FROM ubuntu:20.04

RUN apt update 

# install app dependencies

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt install -y python3-pip && pip install playsound
RUN pip install SpeechRecognition && pip install gtts
RUN apt install -y portaudio19-dev && pip3 install pyaudio
RUN apt install -y libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
RUN pip3 install pycairo && pip3 install pygobject