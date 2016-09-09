from socket import *

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(('localhost', 6001))
tcp_server.listen(1)

while(True):
    print 'wait client socket connect'
    client, client_info = tcp_server.accept()
    print client_info
    while(True):
        msg = client.recv(1024)
        if(msg == ''):
            client.close()
        print 'recv', msg
        client.send('echo ' + msg)
        if(msg == 'q'):
            client.close()
            break

tcp_server.close()

