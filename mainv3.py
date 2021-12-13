#pip install SpeechRecognition
#in case of error use 'pip install pyaudio' or...
#in case of error use 'pip install pipwin' then 'pipwin install pyaudio'
#if error continued you may need to use python 3.6 or lower as the latest
#python may not support pyaudio...
import speech_recognition as sr

def check():
    for line in lines:
        if line in query:
            return line

lines = ["act 1 scene 1", "act 1 scene 2", "act 1 scene 3"]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# simple function to recognise speech from user
def takecommand():
    #it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
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
  check()
  print(check())
