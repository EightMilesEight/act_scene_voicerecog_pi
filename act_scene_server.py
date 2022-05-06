# pip3 install adafruit-blinka
# lsmod | grep -i i2c
# sudo i2cdetect -y 1
# pip3 install adafruit-circuitpython-ht16k33
import socket
from threading import *
from tkinter import *
'''
import time
import board
import busio
from adafruit_ht16k33 import segments
# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)
# Clear the display.
display.fill(0)
'''

version = 'Beta v1.3'


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

    def run(self):
        act_scene = 'Unsure'
        win = Tk()
        win.title('Scene Recognizer ' + version)
        scene_lbl = Label(win, text='Current scene: ' + act_scene, font=('Arial'))
        scene_lbl.pack()
        win.update()
        while True:
            act_scene = self.sock.recv(1024).decode()
            print('Client sent:', act_scene)
            scene_lbl.configure(text='Current scene: ' + act_scene)
            win.update()
            '''
            display.print(':')
            display.print(act_scene)
            '''
            self.sock.send(b'Recieved')

serversocket.listen(5)
print ('server started and listening')
startup_win = Tk()
startup_win.title('Scene Recognizer Startup ' + version)
startup_lbl = Label(startup_win, text='Waiting for a client to connect', font=('Arial'))
startup_lbl.pack()
startup_win.update()
while True:
    clientsocket, address = serversocket.accept()
    startup_win.destroy()
    client(clientsocket, address)