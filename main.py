from socket import *
import threading
import sys
# pip install SpeechRecognition
    # in case of error use 'pip install pyaudio' or...
    # in case of error use 'pip install pipwin' then 'pipwin install pyaudio'
    # if error continued you may need to use python 3.6 or lower as the latest
    # python may not support pyaudio...
import speech_recognition as sr

FLAG = False  # this is a flag variable for checking quit

# check if the speech includes phrases from the "lines" list, and return which phrase is included
# the first phrase in the list that is recognized will be returned
def check():
    for line in lines:
        if line in query:
            return line

lines = ["act 1 scene 1", "act 1 scene 2", "act 1 scene 3"]

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

def voice_recog():
    while True:
        query = takecommand()  # whatever user says will be stored in this variable
        print("The Test got in program is : " + query)
        check()
        print(check())
        send_msg = check()
        clsock.sendall(send_msg.encode())

# function for receiving message from client
def send_to_server(clsock):
    global FLAG
    while True:
        if FLAG == True:
            break

        send_msg = check()
        clsock.sendall(send_msg.encode())

# function for receiving message from server
def recv_from_server(clsock):
    global FLAG
    while True:
        data = clsock.recv(1024).decode()
        if data == 'q':
            print('Closing connection')
            FLAG = True
            break
        print('Server: ' + data)

# this is main function
def main():
    threads = []
    # TODO (1) - define HOST name, this would be an IP address or 'localhost' (1 line)
    HOST = 'localhost'  # The server's hostname or IP address
    # TODO (2) - define PORT number (1 line) (Google, what should be a valid port number)
    PORT = 1024       # The port used by the server

    # Create a TCP client socket
    #(AF_INET is used for IPv4 protocols)
    #(SOCK_STREAM is used for TCP)
    # TODO (3) - CREATE a socket for IPv4 TCP connection (1 line)
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # request to connect sent to server defined by HOST and PORT
    # TODO (4) - request a connection to the server (1 line)
    clientSocket.connect((HOST, PORT))
    print('Client is connected to a chat sever!\n')



    # call the function to send message to server
    #send_to_server(clientSocket)
    t_send = threading.Thread(target=send_to_server, args=(clientSocket,))
    # call the function to receive message server
    #recv_from_server(clientSocket)
    t_rcv = threading.Thread(target=recv_from_server, args=(clientSocket,))
    threads.append(t_send)
    threads.append(t_rcv)
    t_send.start()
    t_rcv.start()

    t_send.join()
    t_rcv.join()

    print('EXITING')
    sys.exit()

# This is where the program starts
if __name__ == '__main__':
    main()