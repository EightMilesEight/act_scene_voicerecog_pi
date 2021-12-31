# pip3 install adafruit-blinka
# lsmod | grep -i i2c
# sudo i2cdetect -y 1
# pip3 install adafruit-circuitpython-ht16k33
import socket
from threading import *
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

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1024
print ('Host: ',host)
print ('Port: ',port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while True:
            act_scene = self.sock.recv(1024).decode()
            print('Client sent:',act_scene)
            '''
            display.print(':')
            display.print(act_scene)
            '''
            self.sock.send(b'Recieved')

serversocket.listen(5)
print ('server started and listening')
while True:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)