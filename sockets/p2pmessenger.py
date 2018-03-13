import socket
import threading

ENCODING = 'utf-8'

#simple messenger has two components, a sender and a receiver.
#These two components should run on separated threads
#To implement them we will have two classes: Receiver and Sender. Both of them will extend threading.Thread

#The receiver is the one responsible of receiving messages. It will be a component which binds a server socket to listen to connections and receive the data the client is sending.
class Receiver(threading.Thread):
    def __init__(self, my_host, my_port):
        threading.Thread.__init__(self, name="messenger_receiver")
        self.host = my_host
        self.port = my_port

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Create a new socket using the AF_INET address family, and SOCK_STREAM socket type
        sock.bind((self.host, self.port))
        sock.listen(10)
        while True:
            connection, client_address = sock.accept()
            try:
                full_message = ""
                while True:
                    data = connection.recv(16)
                    full_message = full_message + data.decode(ENCODING)
                    if not data:
                        print("{}: {}".format(client_address, full_message.strip()))
                        break
            finally:
                connection.shutdown(2)
                connection.close()

    def run(self):
        self.listen()

#The sender is the one responsible of sending messages. In most cases, it’s a component which, every time the user wants to send a message, opens a client socket, connects it to the recipient of the message, actually sends the message and then closes the socket.
class Sender(threading.Thread):
    def __init__(self, my_friends_host, my_friends_port):
        threading.Thread.__init__(self, name="messenger_sender")
        self.host = my_friends_host
        self.port = my_friends_port

    def run(self):
        while True:
            message = input("=>") #collect message from terminal input
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port)) #sender socket connects rather than binds and listen
            s.sendall(message.encode(ENCODING))
            s.shutdown(2)
            s.close()



def main():
    my_host = input("which is my host? ")
    my_port = int(input("which is my port? "))
    receiver = Receiver(my_host, my_port)
    my_friends_host = input("what is your friend's host? ")
    my_friends_port = int(input("what is your friend's port? "))
    sender = Sender(my_friends_host, my_friends_port)
    threads = [receiver.start(), sender.start()]

if __name__ == '__main__':
    main()

