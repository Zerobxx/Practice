import os
from multiprocessing import Process, Queue

Qmsg = Queue()
print "Main Pid =", os.getpid()

def chaild_func(name):
    print "Chaild Pid =", os.getpid()
    msg = Qmsg.get()
    print "Name = %s, msg = %s" % (name, msg)

p = Process(target=chaild_func, args=('test',))
Qmsg.put('Process test!')
p.start()
p.join()
