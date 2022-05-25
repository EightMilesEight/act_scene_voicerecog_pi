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
        self.sock = socket
        self.addr = address
        self.start()

    def open_lines(self):
        text_box.delete(0.0, END)
        lines = open('lines.txt', 'r')
        text_box.insert(END, lines.read())
        lines.close()

    def save_lines(self):
        global current_screen
        lines = open('lines.txt', 'w')
        lines.write(text_box.get(1.0, END))
        lines.close()
        text_box.destroy()
        open_btn.destroy()
        save.destroy()
        current_screen = 1

    def GUI_start(self):
        global win
        global text_box
        global open_btn
        global save
        global speech_lbl
        global song_lbl
        global scene_lbl
        global status_lbl
        global current_screen

        current_screen = 0

        # Create an instance of tkinter window
        win = Tk()
        win.title('Scene Recognizer ' + version)

        # Creating a text box widget
        text_box = Text(win)
        text_box.pack()

        open_btn = Button(win, text='Reset to Previous Lines', command=self.open_lines)
        open_btn.pack()

        # Create a button to save the text
        save = Button(win, text='Save Lines', command=self.save_lines)
        save.pack()

        self.open_lines()

        while True:
            if current_screen == 0:
                win.update()
            elif current_screen == 1:
                speech_lbl = Label(win, text='Last speech recognized: ' + speech)
                speech_lbl.pack()
                song_lbl = Label(win, text='Last song recognized: ' + song)
                song_lbl.pack()
                scene_lbl = Label(win, text='Current scene: ' + scene)
                scene_lbl.pack()
                status_lbl = Label(win, text='Current status: ' + status)
                status_lbl.pack()
                win.update()
                break

    # check if the speech includes a phrase, and return which phrase is included
    # the first phrase in the list that is recognized will be returned
    # for some reason it has an error with - and ' so until I fix that don't use lines containing them
    def check(self, phrase):
        for line in lines:
            if line in phrase:
                return line

    def create_markers(self):
        y = 0
        x = 0
        while True:
            try:
                x += 1
                marker = 'act %d scene %d' % (y, x)
                markers[marker] = lines.index(marker)
            except ValueError:
                if y <= 10:
                    y += 1
                    x = 0
                else:
                    marker = '<end>'
                    markers[marker] = lines.index(marker)
                    break

    def find_scene(self, thing_to_check):
        for i in list(markers.values()):
            if lines.index(self.check(thing_to_check)) in range(i, list(markers.values())[list(markers.values()).index(i) + 1]):
                return '0' + list(markers)[list(markers.values()).index(i)][4] + \
                       list(markers)[list(markers.values()).index(i)][-2].replace(' ', '0') + \
                       list(markers)[list(markers.values()).index(i)][-1].replace(' ', '0')

    # simple function to recognise speech from user
    def takecommand(self):
        global song
        if __name__ == '__main__':

            # create a Dejavu instance
            djv = Dejavu(config)

            # Fingerprint all the mp3's in the directory we give it
            djv.fingerprint_directory('mp3', ['.mp3'])

            #	 Or recognize audio from your microphone for `secs` seconds
            secs = 5
            song = 'No songs recognized'
            song = djv.recognize(MicrophoneRecognizer, seconds=secs)
            if song is None or song == 'No songs recognized':
                song = 'No songs recognized'
                song_lbl.configure(text=song)
                win.update()
                print(song)
                return song
            else:
                song = song['song_name']
                song_lbl.configure(text='Last song recognized: ' + song)
                win.update()
                print(song)
                return song

    def run(self):
        global lines
        global scene
        global status
        global speech
        global song
        with open('lines.txt') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            lines = list(filter(None, lines))
        self.create_markers()
        self.GUI_start()
        # creates a list called 'lines' out of lines.txt and strips special characters
        with open('lines.txt') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            lines = list(filter(None, lines))
        while True:
            song = 'No songs recognized'
            song = self.takecommand()  # whatever user says will be stored in this variable
            if self.check(song) != None:
                print(self.check(song))
                scene = self.find_scene(song)
                scene_lbl.configure(text='Current scene: ' + scene)
                win.update()
                print(scene)
                self.sock.send(scene.encode('UTF-8'))


serversocket.listen(5)
print ('server started and listening')
while True:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)