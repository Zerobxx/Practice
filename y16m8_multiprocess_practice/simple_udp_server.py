from socket import *

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(('localhost', 6002))

while(True):
    client_data, addr = udp_server.recvfrom(1024)
    print 'recv', client_data, 'from', addr
    udp_server.sendto('echo ' + client_data, addr)
    if(client_data == 'q'):
        break

udp_server.close()