import threading, Queue
import time

g_queue = Queue.Queue()

def func():
    global g_queue

    while True:
        msg = g_queue.get()
        print "receive msg =", msg

if __name__ == '__main__':
    t = threading.Thread(target=func, args=())
    t.setDaemon(True)
    t.start()

    tmp = 0
    while True:
        tmp += 1
        print 'send msg =', tmp
        g_queue.put(tmp)
        time.sleep(1)
    t.join()