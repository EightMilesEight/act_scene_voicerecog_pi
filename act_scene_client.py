import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1024
s.connect((host, port))

# pip install SpeechRecognition
# in case of error use 'pip install pyaudio' or...
# in case of error use 'pip install pipwin' then 'pipwin install pyaudio'
# if error continued you may need to use python 3.6 or lower as the latest
# python may not support pyaudio...
import speech_recognition as sr

# Import tkinter library
from tkinter import *

version = 'Beta v1.1'

def open_lines():
    text_box.delete(0.0, END)
    lines = open("lines.txt", "r")
    text_box.insert(END, lines.read())
    lines.close()

def save_lines():
    lines = open("lines.txt", "w")
    lines.write(text_box.get(1.0, END))
    lines.close()
    win.destroy()

def GUI_start():
    global text_box
    global open_btn
    global save
    # Creating a text box widget
    text_box = Text(win)
    text_box.pack()

    open_btn = Button(win, text="Reset to Previous Lines", command=open_lines)
    open_btn.pack()

    # Create a button to save the text
    save = Button(win, text="Save Lines", command=save_lines)
    save.pack()

    open_lines()

# creates a list called "lines" out of lines.txt
with open('lines.txt') as file:
    global lines
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# check if the speech includes a phrase, and return which phrase is included
# the first phrase in the list that is recognized will be returned
# for some reason it has an error with - and ' so until I fix that don't use lines containing them
def check(phrase):
    for line in lines:
        if line in phrase:
            return line


A1S1 = lines.index(check('act 1 scene 1'))
A1S2 = lines.index(check('act 1 scene 2'))
A1S3 = lines.index(check('act 1 scene 3'))
A1S4 = lines.index(check('act 1 scene 4'))
A1S5 = lines.index(check('act 1 scene 5'))
A1S6 = lines.index(check('act 1 scene 6'))
A1S7 = lines.index(check('act 1 scene 7'))
A1S8 = lines.index(check('act 1 scene 8'))
A1S9 = lines.index(check('act 1 scene 9'))
A1S10 = lines.index(check('act 1 scene 10'))
A1S11 = lines.index(check('act 1 scene 11'))
A1S12 = lines.index(check('act 1 scene 12'))
A1S13 = lines.index(check('act 1 scene 13'))
A1S14 = lines.index(check('act 1 scene 14'))
A1S15 = lines.index(check('act 1 scene 15'))
A2S1 = lines.index(check('act 2 scene 1'))
A2S2 = lines.index(check('act 2 scene 2'))
A2S3 = lines.index(check('act 2 scene 3'))
A2S4 = lines.index(check('act 2 scene 4'))
A2S5 = lines.index(check('act 2 scene 5'))
A2S6 = lines.index(check('act 2 scene 6'))
A2S7 = lines.index(check('act 2 scene 7'))
A2S8 = lines.index(check('act 2 scene 8'))
A2S9 = lines.index(check('act 2 scene 9'))
A2S10 = lines.index(check('act 2 scene 10'))
A2S11 = lines.index(check('act 2 scene 11'))
A2S12 = lines.index(check('act 2 scene 12'))
A2S13 = lines.index(check('act 2 scene 13'))
A2S14 = lines.index(check('act 2 scene 14'))
A2S15 = lines.index(check('act 2 scene 15'))
A3S1 = lines.index(check('act 3 scene 1'))
A3S2 = lines.index(check('act 3 scene 2'))
A3S3 = lines.index(check('act 3 scene 3'))
A3S4 = lines.index(check('act 3 scene 4'))
A3S5 = lines.index(check('act 3 scene 5'))
A3S6 = lines.index(check('act 3 scene 6'))
A3S7 = lines.index(check('act 3 scene 7'))
A3S8 = lines.index(check('act 3 scene 8'))
A3S9 = lines.index(check('act 3 scene 9'))
A3S10 = lines.index(check('act 3 scene 10'))
A3S11 = lines.index(check('act 3 scene 11'))
A3S12 = lines.index(check('act 3 scene 12'))
A3S13 = lines.index(check('act 3 scene 13'))
A3S14 = lines.index(check('act 3 scene 14'))
A3S15 = lines.index(check('act 3 scene 15'))
end = lines.index(check('end'))


def find_scene():
    if (lines.index(check(speech))) in range(A1S1, A1S2):
        return '0101'
    elif (lines.index(check(speech))) in range(A1S2, A1S3):
        return '0102'
    elif (lines.index(check(speech))) in range(A1S3, A1S4):
        return '0103'
    elif (lines.index(check(speech))) in range(A1S4, A1S5):
        return '0104'
    elif (lines.index(check(speech))) in range(A1S5, A1S6):
        return '0105'
    elif (lines.index(check(speech))) in range(A1S6, A1S7):
        return '0106'
    elif (lines.index(check(speech))) in range(A1S7, A1S8):
        return '0107'
    elif (lines.index(check(speech))) in range(A1S8, A1S9):
        return '0108'
    elif (lines.index(check(speech))) in range(A1S9, A1S10):
        return '0109'
    elif (lines.index(check(speech))) in range(A1S10, A1S11):
        return '0110'
    elif (lines.index(check(speech))) in range(A1S11, A1S12):
        return '0111'

# simple function to recognise speech from user
def takecommand():
    # it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)
    try:
        print('Recognising...')
        speech = r.recognize_google(audio, language='en-in')
        print('User Said : ', speech)
    except Exception as e:
        print('exception : ', e)
        return "None"
    return speech


def ts(str):
    s.sendall(r.encode('utf-8'))
    data = ''
    data = s.recv(1024).decode()
    print(data)

# Create an instance of tkinter window
win = Tk()
win.title('Scene Recognizer ' + version)
win.geometry("600x325")
GUI_start()
win.mainloop()
while True:
    # creates a list called "lines" out of lines.txt
    with open('lines.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    speech = takecommand()  # whatever user says will be stored in this variable
    print("The Test got in program is: " + speech)
    if check(speech) and find_scene() != None:
        print(check(speech))
        r = find_scene()
        print(r)
        ts(s)
