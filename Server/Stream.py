# Stream receives a video stream from the client and displays it on the screen.
import socket
import numpy as np
import cv2


class VideoStreamingTest(object):
    def __init__(self, connection, add):

        # Capture connection information.
        self.connection = connection
        self.client_address = add
        self.connection1 = connection.makefile('rb')
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)

        # Start Stream
        self.streaming()

    # Method for receiving stream over a socket
    def streaming(self):
        try:
            print("Host: ", self.host_name + ' ' + self.host_ip)
            print("Connection from: ", self.client_address)
            print("Streaming...")
            print("Press 'q' to exit")

            stream_bytes = b' '
            while True:
                stream_bytes += self.connection1.read(1024)
                first = stream_bytes.find(b'\xff\xd8')
                last = stream_bytes.find(b'\xff\xd9')
                if first != -1 and last != -1:
                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]
                    image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    cv2.imshow('image', image)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        finally:
            self.connection.close()
