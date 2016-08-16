import os
from multiprocessing import Queue

Qmsg = Queue()
pid = os.fork()

if(pid==0):
    print 'in subprocess pid = %d' % os.getpid()
    msg = Qmsg.get()
    print 'subprocess get Queue msg %s' % msg
else:
    print 'in mainprocess pid = %d' % os.getpid()
    Qmsg.put('test msg')
    os.wait()