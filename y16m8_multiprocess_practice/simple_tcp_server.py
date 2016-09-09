from socket import *
import time

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(('localhost', 6001))
tcp_server.listen(5)
time.sleep(10)
print "tcp_server wait tcp connect"
client, client_info=tcp_server.accept()
client_data = client.recv(1024)
print client_data, "-tcp_server receive data"
client.close()
tcp_server.close()

