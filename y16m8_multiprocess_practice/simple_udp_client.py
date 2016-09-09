from socket import *

udp_client = socket(AF_INET, SOCK_DGRAM)
while(True):
    msg = raw_input('>')
    udp_client.sendto(msg, ('localhost', 6002))
    rmsg, addr = udp_client.recvfrom(1024)
    print rmsg, addr
    if(msg == 'q'):
        break

udp_client.close()


