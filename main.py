#pip install SpeechRecognition
#in case of error use 'pip install pyaudio' or...
#in case of error use 'pip install pipwin' then 'pipwin install pyaudio'
#if error continued you may need to use python 3.6 or lower as the latest
#python may not support pyaudio...
import speech_recognition as sr
import pyttsx3

#audio of system to respond
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# simple function to recognise speech from user
def takecommand():
    #it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print('User Said : ' , query)

    except Exception as e:
        print('exception : ',e)
        return "None"
    return query
while True:
  query = takecommand() # whatever user says will be stored in this variable
  print("The Test got in program is : "+query)

  A1S1 = "Act 1 Scene 1"
  A1S2 = "Act 1 Scene 2"
  A1S3 = "Act 1 Scene 3"
  A1S4 = "Act 1 Scene 4"
  A1S5 = "Act 1 Scene 5"
  A1S6 = "Act 1 Scene 6"
  A1S7 = "Act 1 Scene 7"
  A1S8 = "Act 1 Scene 8"
  A1S9 = "Act 1 Scene 9"
  A2S1 = "Act 2 Scene 1"
  A2S2 = "Act 2 Scene 2"
  A2S3 = "Act 2 Scene 3"
  A2S4 = "Act 2 Scene 4"
  A2S5 = "Act 2 Scene 5"
  A2S6 = "Act 2 Scene 6"
  A2S7 = "Act 2 Scene 7"
  A2S8 = "Act 2 Scene 8"
  A2S9 = "Act 2 Scene 9"
  A3S1 = "Act 3 Scene 1"
  A3S2 = "Act 3 Scene 2"
  A3S3 = "Act 3 Scene 3"
  A3S4 = "Act 3 Scene 4"
  A3S5 = "Act 3 Scene 5"
  A3S6 = "Act 3 Scene 6"
  A3S7 = "Act 3 Scene 7"
  A3S8 = "Act 3 Scene 8"
  A3S9 = "Act 3 Scene 9"

  if A1S1.lower() in query.lower():
      print(A1S1)
  elif A1S2.lower() in query.lower():
      print(A1S2)
  elif A1S3.lower() in query.lower():
      print(A1S3)
  elif A1S4.lower() in query.lower():
      print(A1S4)
  elif A1S5.lower() in query.lower():
      print(A1S5)
  elif A1S6.lower() in query.lower():
      print(A1S6)
  elif A1S7.lower() in query.lower():
      print(A1S7)
  elif A1S8.lower() in query.lower():
      print(A1S8)
  elif A1S9.lower() in query.lower():
      print(A1S9)
  elif A2S1.lower() in query.lower():
      print(A2S1)
  elif A2S2.lower() in query.lower():
      print(A2S2)
  elif A2S3.lower() in query.lower():
      print(A2S3)
  elif A2S4.lower() in query.lower():
      print(A2S4)
  elif A2S5.lower() in query.lower():
      print(A2S5)
  elif A2S6.lower() in query.lower():
      print(A2S6)
  elif A2S7.lower() in query.lower():
      print(A2S7)
  elif A2S8.lower() in query.lower():
      print(A2S8)
  elif A2S9.lower() in query.lower():
      print(A2S9)
  elif A3S1.lower() in query.lower():
      print(A3S1)
  elif A3S2.lower() in query.lower():
      print(A3S2)
  elif A3S3.lower() in query.lower():
      print(A3S3)
  elif A3S4.lower() in query.lower():
      print(A3S4)
  elif A3S5.lower() in query.lower():
      print(A3S5)
  elif A3S6.lower() in query.lower():
      print(A3S6)
  elif A3S7.lower() in query.lower():
      print(A3S7)
  elif A3S8.lower() in query.lower():
      print(A3S8)
  elif A3S9.lower() in query.lower():
      print(A3S9)
  else:
      print("")