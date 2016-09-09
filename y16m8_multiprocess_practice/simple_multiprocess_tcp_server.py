import os
from socket import *
import sys

def client_deal(client, client_info):
    while(True):
        msg = client.recv(1024)
        print 'msg=', msg, 'from', client_info
        if(msg == ''):
            client.close()
            break
        client.send('echo '+msg)
        if(msg == 'q'):
            client.close()
            break

def client_process(client, client_info):
    pid = os.fork()
    if(pid == 0):
        ppid = os.fork()
        if(ppid == 0):
            client_deal(client, client_info)
        else:
            print os.getpid(), 'child exit'
        sys.exit()
    else:
        client.close()
        os.wait()
        print 'main process recycle child process'

if __name__ == '__main__':
    tcp_server = socket(AF_INET, SOCK_STREAM)
    tcp_server.bind(('localhost', 6001))
    tcp_server.listen(5)
    while(True):
        print os.getpid(), 'wait client'
        client, client_info = tcp_server.accept()
        print client_info
        client_process(client, client_info)

    tcp_server.close()
