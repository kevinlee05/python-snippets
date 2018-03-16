#https://benediktkr.github.io/dev/2016/02/04/p2p-with-twisted.html

from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.protocol import Protocol, Factory
from twisted.inernet import reactor

import json

class MyProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.state = "HELLO"
        self.remote_nodeid = None
        self.nodeid = self.factory.nodeid

#The Factory class instance is persistent between connections, so it’s where we store things like the peer list and the UUID for this session. A new instance of MyFactoryis created for each connection.
class MyFactory(Factory):
    def startFactory(self):
        self.peers = {}
        self.nodeid = generate_nodeid()

    def buildProtocol(self, addr):
        return NCProtocol(self)

#This will define a listener for a completely empty protocol on localhost:5999
endpoint = TCP4ServerEndpoint(reactor, 5999)
endpoint.listen(MyFactory())
