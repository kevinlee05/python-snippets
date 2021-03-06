###########################################################################
# Concurrent server - webserver3e.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import os
import signal
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5

def grim_reaper(signum, frame):
    pid, status = os.wait() #wait for child process to terminate and return status information
    print(
        'Child {pid} terminated with status {status}'
        '\n'.format(pid=pid, status=status)
    )

def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
        HTTP/1.1 200 OK

        Hello, World!
        """
    client_connection.sendall(http_response)
    # sleep to allow the parent to loop over to 'accept' and block there
    time.sleep(3)

def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper) #When a child process stops or terminates, SIGCHLD is sent to the parent process.
    #The default response to the signal is to ignore it. The signal can be caught and the exit status from the child process can be obtained by immediately calling os.wait()  - see grim_reaper function

    while True:
        client_connection, client_address = listen_socket.accept()
        pid = os.fork()
        if pid == 0: #pid will be 0 if the process is the child
            listen_socket.close() #close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else: #pid will not be 0 if the process is parent
            client_connection.close()

if __name__ == '__main__':
    serve_forever()






