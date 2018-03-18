#http://twistedmatrix.com/documents/current/core/howto/servers.html
#ported to python3
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Chat(LineReceiver):
    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        self.sendLine(b"Whats your name?") #sendLine accepts bytes only

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine(b"Name taken, please choose another.")
            return
        self.sendLine("Welcome, {}!".format(name.decode()).encode('utf-8'))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name.decode(), message.decode())
        for name, protocol in self.users.items(): #iteritems => items for python3
            if protocol != self:
                protocol.sendLine(message.encode('utf-8'))

class ChatFactory(Factory):

    def __init__(self):
        self.users = {} #maps user names to Chat instances

    def buildProtocol(self, addr):
        return Chat(self.users)

#listenTCP is the method which connects a Factory to the network. This is the lower-level API that endpoints wraps for you.
reactor.listenTCP(8123, ChatFactory())
reactor.run()
