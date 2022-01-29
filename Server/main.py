# Main Connects to the client and sends controller inputs to client.
import socket
import time
import Stream
from threading import Thread
import Controller as joyStick

# Start server
socketserver = socket.socket()
host = '192.168.1.70'
port = 8000
socketserver.bind((host, port))
socketserver.listen(5)

# Wait for client connection.
clientSocket, address = socketserver.accept()

# Start video streaming thread
thread = Thread(target=Stream.VideoStreamingTest, args=(clientSocket, address))
thread.start()


# While the connection is good, send controller inputs to client.
def main():
    jsVal = joyStick.getJS()

    # Convert input to binary and send to client.
    clientSocket.send(bin(int(jsVal['axis2'] * 100)).encode())
    clientSocket.send(bin(int(jsVal['axis1'] * 100)).encode())

    # Delay to not overwhelm the client.
    time.sleep(.1)


if __name__ == '__main__':
    while True:
        main()
