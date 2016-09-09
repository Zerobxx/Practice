from socket import *

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(('localhost', 6001))

while(True):
    msg = raw_input('>')
    tcp_client.send(msg)
    rmsg = tcp_client.recv(1024)
    print rmsg
    if(msg == 'q'):
        tcp_client.close()
        break