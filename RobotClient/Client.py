# Import socket module
import socket
import StreamClient as StreamStart
from MotorModuleTest import Motor
from threading import Thread

# Create motor object
motor = Motor(2, 3, 4, 22, 17, 27)

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8000

# connect to the server on local computer
s.connect(('', port))

# Start video stream
thread = Thread(target=StreamStart.stream, args=(s,))
thread.start()

def main():
    # receive data from the server and decoding to get the string.
    try:
        axis1 = (int(s.recv(1024).decode(), 2) / 100)
        axis2 = (int(s.recv(1024).decode(), 2) / 100)
        motor.move(-axis1, axis2, 0.1)
    except ValueError:
        pass


if __name__ == '__main__':
    while True:
        main()
