#https://ruslanspivak.com/lsbaws-part2/

import socket
import StringIO
import sys

class WSGIServer(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        #Create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        # Allow to reuse the seame address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind
        listen_socket.bind(server_address)
        # Activate
        listen_socket.listen(self.request_queue_size)
        # Get server host name and port
        # getsockname() Returns the socket’s own address
        host, port = self.listen_socket.getsockname()[:2]
        #get fully qualified domain name of host
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        # headers_set to be set by wsgi Web framework/Web application
        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            # New client connection
            self.client_connection, client_address = listen_socket.accept()
            # Handle one request and close the client connection. Then loop over to wait for another client connection
            self.handle_one_request()

        def handle_one_request(self):
            self.request_data = request_data = self.client_connection.recv(1024)









