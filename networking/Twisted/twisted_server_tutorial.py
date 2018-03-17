#http://twistedmatrix.com/documents/current/core/howto/servers.html
#Your protocol handling class will usually subclass twisted.internet.protocol.Protocol. Most protocol handlers inherit either from this class or from one of its convenience children. An instance of the protocol class is instantiated per-connection, on demand, and will go away when the connection is finished. This means that persistent configuration is not saved in the Protocol.
#The persistent configuration is kept in a Factory class, which usually inherits from twisted.internet.protocol.Factory. The buildProtocol method of the Factory is used to create a Protocol for each new connection.

from twisted.internet.protocol import Protocol

class Echo(Protocol):

    def dataReceived(self, data):
        self.transport.write(data)

class QOTD(Protocol):

    #The connectionMade event is usually where setup of the connection object happens, as well as any initial greetings
    def connectionMade(self):
        self.transport.write("an apple a day keeps twisted away\r\n")
        """loseConnection is called immediately after writing to the transport. The loseConnection call will close the connection only when all the data has been written by Twisted out to the operating system"""
        self.transport.loseConnection()

class Echo(Protocol):
    """Here connectionMade and connectionLost cooperate to keep a count of the active protocols in a shared object, the factory. The factory must be passed to Echo.__init__ when creating a new instance. The factory is used to share state that exists beyond the lifetime of any given connection. """
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1

        self.transport.write(
            "Welcome! There are currently %d open connections. \n" %
            (self.factory.numProtocols, ))

    #The connectionLost event is where tearing down of any connection-specific objects is done.
    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self, data):
        self.transport.write(data)

