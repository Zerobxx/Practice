from socket import *
import select
import Queue


if __name__ == '__main__':
    tcp_server = socket(AF_INET, SOCK_STREAM)
    tcp_server.bind(('localhost', 6001))
    tcp_server.listen(10)

    msg_list = {}
    in_list = []
    out_list = []
    in_list.append(tcp_server)

    while(True):
        rlist, wlist, elist = select.select(in_list, out_list, in_list, 3)

        if(not (rlist or wlist or elist)):
            print 'Wait Timeout: in_list =', len(in_list)
            continue

        for c in rlist:
            if(c == tcp_server):
                client, client_info = tcp_server.accept()
                in_list.append(client)
                msg_list[client] = Queue.Queue()

            else:
                msg = c.recv(1024)
                if(msg):
                    print 'recv', msg
                    msg_list[c].put('echo ' + msg)
                    if(c not in out_list):
                        out_list.append(c)
                else:
                    if(c in out_list):
                        out_list.remove(c)
                    in_list.remove(c)
                    c.close()
                    del msg_list[c]
                    print 'a client exit'

        for c in elist:
            if(c in in_list):
                in_list.remove(c)
            if(c in out_list):
                out_list.remove(c)
            c.close()
            del msg_list[c]

        for c in wlist:
            if(c in msg_list):
                try:
                    msg = msg_list[c].get_nowait()
                except Queue.Empty:
                    out_list.remove(c)
                else:
                    print 'send to client:', msg
                    c.send(msg)

    tcp_server.close()


