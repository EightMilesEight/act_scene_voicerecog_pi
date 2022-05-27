# future me: if you're getting the HY000 with MySQL error, try su -, then cd /, mkdir -p /var/run/mysqld, then chown mysql:mysql /var/run/mysqld, then mysqld_safe &, then mysql -u root -p, then CREATE DATABASE IF NOT EXISTS dejavu;
# if that doesn't work, completely reinstall MySQL, ake sure you use apt purge, then try the above again
# if that doesn't work, you're toast, because I'm not even sure why this worked, and it didn't the first few times
# mysqld --initialize might have done something, so try that, I guess. Godspeed.

import json
import warnings

warnings.filterwarnings('ignore')

from dejavu import Dejavu
from dejavu.recognize import MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open('dejavu.cnf') as f:
    config = json.load(f)

import socket
import time
from threading import *

# pip install SpeechRecognition
# in case of error use 'pip install pyaudio' or...
# in case of error use 'pip install pipwin' then 'pipwin install pyaudio'
# if error continued you may need to use python 3.6 or lower as the latest
import speech_recognition as sr
from tkinter import *

import sys

version = 'Beta v1.4'
speech = ''
song = ''
scene = 'Unsure'
status = ''
markers = {}
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1024
print('Host: ', host)
print('Port: ', port)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.version = version
        self.speech = speech
        self.song = song
        self.scene = scene
        self.status = status
        self.markers = markers
        self.sock = socket
        self.addr = address
        self.start()

    def open_lines(self):
        self.text_box.delete(0.0, END)
        self.lines = open('lines.txt', 'r')
        self.text_box.insert(END, self.lines.read())
        self.lines.close()

    def save_lines(self):
        self.lines = open('lines.txt', 'w')
        self.lines.write(self.text_box.get(1.0, END))
        self.lines.close()
        self.text_box.destroy()
        self.open_btn.destroy()
        self.save.destroy()
        self.current_screen = 1

    def GUI_start(self):

        self.current_screen = 0

        # Create an instance of tkinter window
        self.win = Tk()
        self.win.title('Scene Recognizer ' + version)

        # Creating a text box widget
        self.text_box = Text(self.win)
        self.text_box.pack()

        self.open_btn = Button(self.win, text='Reset to Previous Lines', command=self.open_lines)
        self.open_btn.pack()

        # Create a button to save the text
        self.save = Button(self.win, text='Save Lines', command=self.save_lines)
        self.save.pack()

        self.open_lines()

        while True:
            if self.current_screen == 0:
                self.win.update()
            elif self.current_screen == 1:
                self.speech_lbl = Label(self.win, text='Last speech recognized: ' + self.speech)
                self.speech_lbl.pack()
                self.song_lbl = Label(self.win, text='Last song recognized: ' + self.song)
                self.song_lbl.pack()
                self.scene_lbl = Label(self.win, text='Current scene: ' + self.scene)
                self.scene_lbl.pack()
                self.status_lbl = Label(self.win, text='Current status: ' + self.status)
                self.status_lbl.pack()
                self.win.update()
                break

    # check if the speech includes a phrase, and return which phrase is included
    # the first phrase in the list that is recognized will be returned
    # for some reason it has an error with - and ' so until I fix that don't use lines containing them
    def check(self, phrase):
        for line in self.lines:
            if line in phrase:
                return line

    def create_markers(self):
        y = 0
        x = 0
        while True:
            try:
                x += 1
                marker = 'act %d scene %d' % (y, x)
                markers[marker] = self.lines.index(marker)
            except ValueError:
                if y <= 10:
                    y += 1
                    x = 0
                else:
                    marker = '<end>'
                    markers[marker] = self.lines.index(marker)
                    break

    def find_scene(self, thing_to_check):
        for i in list(markers.values()):
            if self.lines.index(self.check(thing_to_check)) in range(i, list(markers.values())[list(markers.values()).index(i) + 1]):
                return '0' + list(markers)[list(markers.values()).index(i)][4] + \
                       list(markers)[list(markers.values()).index(i)][-2].replace(' ', '0') + \
                       list(markers)[list(markers.values()).index(i)][-1].replace(' ', '0')

    # simple function to recognise speech from user
    def recognize_speech(self):
        while True:
            # it takes microphone input and returns string output
            r = sr.Recognizer()
            with sr.Microphone(device_index=1) as source:
                self.status = 'Listening...'
                print(status)
                r.pause_threshold = 0.5
                audio = r.listen(source)
            try:
                self.status = 'Recognizing...'
                print(status)
                self.speech = r.recognize_google(audio, language='en-in')
                print('Speech recognized: ', self.speech)
                self.speech_update_flag = True
            except:
                print('Error: No recognizable speech detected')

    # simple function to recognise speech from user
    def recognize_song(self):
        while True:

            # create a Dejavu instance
            djv = Dejavu(config)

            # Fingerprint all the mp3's in the directory we give it
            djv.fingerprint_directory('mp3', ['.mp3'])

            #	 Or recognize audio from your microphone for `secs` seconds
            secs = 5
            self.song = 'No songs recognized'
            self.song = djv.recognize(MicrophoneRecognizer, seconds=secs)
            self.song_update_flag = True

    def run(self):
        with open('lines.txt') as file:
            self.lines = file.readlines()
            self.lines = [line.rstrip() for line in self.lines]
            self.lines = list(filter(None, self.lines))
        self.create_markers()
        self.GUI_start()
        # creates a list called 'lines' out of lines.txt and strips special characters
        with open('lines.txt') as file:
            self.lines = file.readlines()
            self.lines = [line.rstrip() for line in self.lines]
            self.lines = list(filter(None, self.lines))
        self.song_update_flag = False
        self.speech_update_flag = False
        Thread(target=self.recognize_song).start()
        Thread(target=self.recognize_speech).start()
        while True:
            if self.song_update_flag is True:
                if self.song is None or self.song == 'No songs recognized' or self.song['confidence'] < 5:
                    self.song = 'No songs recognized'
                    self.song_lbl.configure(text=self.song)
                    self.win.update()
                    print(self.song)
                    self.song_update_flag = False
                else:
                    self.song = self.song['song_name']
                    self.song_lbl.configure(text='Last song recognized: ' + self.song)
                    self.win.update()
                    print(self.song)
                    self.song_update_flag = False
                if self.check(self.song) != None:
                    print(self.check(self.song))
                    self.scene = self.find_scene(self.song)
                    self.scene_lbl.configure(text='Current scene: ' + self.scene)
                    self.win.update()
                    print(self.scene)
                    self.sock.send(self.scene.encode('UTF-8'))
            if self.speech_update_flag is True:
                self.speech_lbl.configure(text='Speech recognized: : ' + self.speech)
                if self.check(self.speech) != None:
                    print(self.check(self.speech))
                    self.scene = self.find_scene(self.speech)
                    self.scene_lbl.configure(text='Current scene: ' + self.scene)
                    self.win.update()
                    print(self.scene)
                    self.sock.send(self.scene.encode('UTF-8'))
                self.speech_update_flag = False
            self.win.update()


serversocket.listen(5)
print ('server started and listening')
while True:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)