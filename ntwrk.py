from simple_socket.tcp_server import SimpleTCPServer
from simple_socket.tcp_client import SimpleTCPClient

class Net:
    def __init__(self, srvPort, srvC, srvDC, srvData, cliPort, cliC, cliDC, cliData):
        self.server = SimpleTCPServer(int(srvPort), listenAddress='127.0.0.1')
        self.client = SimpleTCPClient('127.0.0.1', int(cliPort))

        self.server.onConnected = srvC
        self.server.onDisconnected = srvDC
        self.server.onReceive = srvData 

        self.client.onConnected = cliC 
        self.client.onDisconnected = cliDC 
        self.client.onReceive = cliData 
