#http://twistedmatrix.com/documents/current/core/howto/servers.html
#Your protocol handling class will usually subclass twisted.internet.protocol.Protocol. Most protocol handlers inherit either from this class or from one of its convenience children. An instance of the protocol class is instantiated per-connection, on demand, and will go away when the connection is finished. This means that persistent configuration is not saved in the Protocol.
#The persistent configuration is kept in a Factory class, which usually inherits from twisted.internet.protocol.Factory. The buildProtocol method of the Factory is used to create a Protocol for each new connection.

from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

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

class QOTD(Protocol):

    #The connectionMade event is usually where setup of the connection object happens, as well as any initial greetings
    def connectionMade(self):
        self.transport.write("an apple a day keeps twisted away\r\n")
        """loseConnection is called immediately after writing to the transport. The loseConnection call will close the connection only when all the data has been written by Twisted out to the operating system"""
        self.transport.loseConnection()

#create a protocol Factory that its job is to build QOTD protocol instances.
class QOTDFactory(Factory):
    #set its buildProtocol method to return instances of the QOTD class.
    def buildProtocol(self, addr):
        return QOTD()

def runQOTD():
    # listen on a TCP port, so make a TCP4ServerEndpoint to identify the port to bind to, and then pass the factory to its listen method.
    endpoint = TCP4ServerEndpoint(reactor, 8007)
    #endpoint.listen() tells the reactor to handle connections to the endpoint’s address using a particular protocol
    endpoint.listen(QOTDFactory())
    #starts the reactor and then waits forever for connections to arrive on the specified port. reactor can be stopped by reactor.stop()
    #The reactor is the core of the event loop within Twisted -- the loop which drives applications using Twisted. The event loop is a programming construct that waits for and dispatches events or messages in a program.
    reactor.run()


class QOTD2(Protocol):

    def connectionMade(self):
        #self.factory was set by the factory's default buildProtocol:
        self.transport.write(self.factory.quote + '\r\n')
        self.transport.loseConnection()

class QOTD2Factory(Factory):
    """The default implementation of the buildProtocol method calls the protocol attribute of the factory to create a Protocol instance, and then sets an attribute on it called factory which points to the factory itself"""

    # This will be used by the default buildProtocol to create new protocols:
    protocol = QOTD2

    def __init__(self, quote=None):
        self.quote = quote or 'An apple a day keeps the doctor away'

def runQOTD2():
    endpoint = TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(QOTDFactory("configurable quote"))
    reactor.run()


from twisted.protocols.basic import LineReceiver
#LineReceiver protocol handles mixed line-based sections and raw data sections

class Answer(LineReceiver):
    #LineReceiver protocol dispatches to two different event handlers – lineReceived and rawDataReceived
    answers = {'How are you?': 'Fine', None: "I don't know what you mean"}

    def lineReceived(self, line):
        if line in self.answers:
            self.sendLine(self.answers[line])
        else:
            self.sendLine(self.answers[None])


#FACTORY STARTUP AND SHUTDOWN

class LoggingProtocol(LineReceiver):
    """logging protocol to be used in factories to write to a log file"""
    def lineReceived(self, line):
        self.factory.fp.write(line + '\n')

class LogFileFactory(Factory):

    #this factory allows its Protocols to write to a special log-file
    protocol = LoggingProtocol

    def __init__(self, fileName):
        self.file = fileName

    #A Factory has two methods to perform application-specific building up and tearing down
    def startFactory(self):
        self.fp = open(self.file, 'a')

    def stopFactory(self):
        self.fp.close()
