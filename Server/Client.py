# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8000

# connect to the server on local computer
s.connect(('', port))
axis = [0, 0]
while True:
    # receive data from the server and decoding to get the string.
    axis[0] = (int(s.recv(1024).decode(), 2) / 100)
    axis[1] = (int(s.recv(1024).decode(), 2) / 100)
    print(axis)

