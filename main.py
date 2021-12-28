import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1024
s.connect((host,port))

# pip install SpeechRecognition
# in case of error use 'pip install pyaudio' or...
# in case of error use 'pip install pipwin' then 'pipwin install pyaudio'
# if error continued you may need to use python 3.6 or lower as the latest
# python may not support pyaudio...
import speech_recognition as sr

# check if the speech includes phrases from the "lines" list, and return which phrase is included
# the first phrase in the list that is recognized will be returned
# for some reason it has an error with apostrophes so until I fix that I wouldn't use them
def check():
   with open('lines.txt') as file:
      global lines
      lines = file.readlines()
      lines = [line.rstrip() for line in lines]
      for line in lines:
         if line in query:
            return line

def find_scene():
      if (lines.index(check())) < 7:
         return '0101'
      elif (lines.index(check())) < 40:
         return '0102'
      elif (lines.index(check())) < 55:
         return '0103'
      elif (lines.index(check())) < 75:
         return '0104'
      elif (lines.index(check())) < 93:
         return '0105'
      elif (lines.index(check())) < 109:
         return '0106'
      elif (lines.index(check())) < 116:
         return '0107'
      elif (lines.index(check())) < 129:
         return '0108'
      elif (lines.index(check())) < 144:
         return '0109'
      elif (lines.index(check())) < 162:
         return '0110'
      elif (lines.index(check())) < 173:
         return '0111'
      else:
         return None

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
      query = r.recognize_google(audio, language='en-in')
      print('User Said : ', query)
   except Exception as e:
      print('exception : ', e)
      return "None"
   return query

def ts(str):
   s.sendall(r.encode('utf-8'))
   data = ''
   data = s.recv(1024).decode()
   print (data)

while 2:
   query = takecommand()  # whatever user says will be stored in this variable
   print("The Test got in program is: " + query)
   check()
   if check() != None:
      print(check())
      r = find_scene()
      ts(s)
      print(find_scene())

s.close()