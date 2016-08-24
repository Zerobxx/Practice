import time
from multiprocessing import Process, Queue

Qmsg = Queue()

def child_func():
    while(True):
        msg = Qmsg.get()
        print 'get msg', msg
        if(msg == 'q'):
            break
        time.sleep(3)
        print msg + 'finished'

p = Process(target= child_func, args=())
p.start()

while(True):
    msg = raw_input('>')
    Qmsg.put(msg)
    if(msg == 'q'):
        break

p.join()