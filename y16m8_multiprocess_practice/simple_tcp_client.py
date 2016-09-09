from socket import *

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(('localhost', 6001))
tcp_client.send('Hello Python!')
tcp_client.close()