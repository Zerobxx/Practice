#a simple practice about threading semaphore
import threading
import time

g_sem = threading.Semaphore(1)
# g_sem.release()

def func():
    global g_sem

    print '%s start to acquire semaphore' % threading.currentThread().getName()
    g_sem.acquire()
    print '%s got semaphore & start to sleep ' % threading.currentThread().getName()
    time.sleep(5)
    print '%s release semaphore' % threading.currentThread().getName()
    g_sem.release()

if __name__ == '__main__':
    t = threading.Thread(target=func, args=())
    t.setDaemon(True)
    t.start()

    print '%s start to acquire semaphore' % threading.currentThread().getName()
    g_sem.acquire()
    print '%s got semaphore & start to sleep ' % threading.currentThread().getName()
    time.sleep(5)
    print '%s release semaphore' % threading.currentThread().getName()
    g_sem.release()
    t.join()


