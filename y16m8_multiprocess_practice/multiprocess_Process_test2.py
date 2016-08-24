import os
from multiprocessing import Process, Queue, Lock
import time

Qmsg = Queue()

lock = Lock()

def child_func(name):
    print 'before acquire lock, Pid = %d' % os.getpid()
    lock.acquire()
    print 'acquired the lock, Pid = %d' % os.getpid()
    Qmsg.put('Child_' + str(name) + 'msg_1_Pid:' + str(os.getpid()))
    time.sleep(1)
    Qmsg.put('Child_' + str(name) + 'msg_2_Pid:' + str(os.getpid()))
    lock.release()
    print 'released the lock, Pid = %d' % os.getpid()

sub_process_list = []

for i in range(10):
    p = Process(target= child_func, args= (i,))
    p.start()
    sub_process_list.append(p)

time.sleep(1)

while(True):
    q = Qmsg.get()
    print q

# for i in range(10):
#     p = sub_process_list[i]
#     p.join()

