import os
import sys
import threading
from socket import *

def client_deal(client, client_info):
    while(True):
        msg = client.recv(1024)
        print 'recv', msg, 'from', client_info
        if(msg == ''):
            client.close()
            break
        client.send('echo ' + msg)
        if(msg == 'q' or msg == 'Q'):
            client.close()
            break
    print 'ended a thread!'


def client_thread(client, client_info):
    client_thread = threading.Thread(target= client_deal, args=(client, client_info))
    client_thread.setDaemon(True)
    client_thread.start()
    print 'start a new thread'

if(__name__ == '__main__'):
    tcp_server = socket(AF_INET, SOCK_STREAM)
    tcp_server.bind(('localhost', 6001))
    tcp_server.listen(5)
    while(True):
        print os.getpid(), 'wait client'
        client, client_info = tcp_server.accept()
        print client_info
        client_thread(client, client_info)

    tcp_server.close()
