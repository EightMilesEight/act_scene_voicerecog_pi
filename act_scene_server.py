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
r = 'Unsure'
status = ''
markers = {}
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
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
        lines = open("lines.txt", "r")
        text_box.insert(END, lines.read())
        lines.close()

    def save_lines(self):
        global current_screen
        lines = open("lines.txt", "w")
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

        open_btn = Button(win, text="Reset to Previous Lines", command=self.open_lines)
        open_btn.pack()

        # Create a button to save the text
        save = Button(win, text="Save Lines", command=self.save_lines)
        save.pack()

        self.open_lines()

        while True:
            if current_screen == 0:
                win.update()
            elif current_screen == 1:
                speech_lbl = Label(win, text='Speech recognized: ' + speech)
                speech_lbl.pack()
                scene_lbl = Label(win, text='Current scene: ' + r)
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

    def find_scene(self):
        for i in list(markers.values()):
            if lines.index(self.check(speech)) in range(i, list(markers.values())[list(markers.values()).index(i) + 1]):
                return '0' + list(markers)[list(markers.values()).index(i)][4] + \
                       list(markers)[list(markers.values()).index(i)][-2].replace(' ', '0') + \
                       list(markers)[list(markers.values()).index(i)][-1].replace(' ', '0')

    # simple function to recognise speech from user
    def takecommand(self):
        # it takes microphone input and returns string output
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            status = 'Listening...'
            status_lbl.configure(text='Current status: ' + status)
            win.update()
            print(status)
            r.pause_threshold = 0.5
            audio = r.listen(source)
        try:
            status = 'Recognizing...'
            status_lbl.configure(text='Current status: ' + status)
            win.update()
            print(status)
            speech = r.recognize_google(audio, language='en-in')
            speech_lbl.configure(text='Speech recognized: : ' + speech)
            win.update()
            print('Speech recognized: ', speech)
        except:
            print('Error: No recognizable speech detected')
            return "None"
        return speech

    def run(self):
        global lines
        global r
        global status
        global speech
        with open('lines.txt') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            lines = list(filter(None, lines))
        self.create_markers()
        self.GUI_start()
        # creates a list called "lines" out of lines.txt and strips special characters
        with open('lines.txt') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            lines = list(filter(None, lines))
        while True:
            speech = self.takecommand()  # whatever user says will be stored in this variable
            if self.check(speech) != None:
                print(self.check(speech))
                r = self.find_scene()
                scene_lbl.configure(text='Current scene: ' + r)
                win.update()
                print(r)
                self.sock.send(r.encode("UTF-8"))


serversocket.listen(5)
print ('server started and listening')
while True:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)