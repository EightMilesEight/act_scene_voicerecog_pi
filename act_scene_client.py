import socket
from threading import *
from tkinter import *
import time

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
status = ''

act_scene = 'Unsure'
win = Tk()
win.title('Scene Recognizer ' + version)
scene_lbl = Label(win, text='Current scene: ' + act_scene, font=('Arial'))
scene_lbl.pack()
win.update()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1024
while True:
    try:
        s.connect((host, port))
        break
    except:
        time.sleep(3)
while True:
    act_scene = s.recv(1024).decode()
    print('Client sent:', act_scene)
    scene_lbl.configure(text='Current scene: ' + act_scene)
    win.update()
    '''
    display.print(':')
    display.print(act_scene)
    '''
    s.sendall(b'Recieved')
