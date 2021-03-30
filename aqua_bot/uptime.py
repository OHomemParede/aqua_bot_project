from os import getenv
from threading import Thread
import socket

def send_ok():
  while True:
    connection, _ = TCP.accept()
    connection.send('HTTP/1.1 200 OK'.encode())
    connection.close()


HOST = '127.0.0.1'
PORT = getenv('PORT')

TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ORIGIN = (HOST, PORT)

TCP.bind(ORIGIN) 
TCP.listen()

Thread(target=send_ok, args=()).start()
