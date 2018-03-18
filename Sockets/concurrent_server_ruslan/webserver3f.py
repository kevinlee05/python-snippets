###########################################################################
# Concurrent server - webserver3f.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import errno
import os
import signal
import socket

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 1024


def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1, #Wait for any child process
                os.WHOHANG #Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0: #no more zombies
            return


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)

def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    #Use the SIGCHLD event handler to asynchronously wait for a terminated child to get its termination status
    signal.signal(signal.SIGCHLD, grim_reaper)


    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        #handle errors thrown when listen_socket.accept() is interrupted
        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            # Many system calls will report the EINTR error code if a signal occurred while the system call was in progress.
            if code == errno.EINTR:
                # the system will not resume automatically so you need to catch the error and manually continue
                continue
            else:
                raise

        pid = os.fork()

        if pid == 0: # child
            listen_socket.close() #close child coppy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else: #parent
            client_connection.close()

if __name__ == '__main__':
    serve_forever()
