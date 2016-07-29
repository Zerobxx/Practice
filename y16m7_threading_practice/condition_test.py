#a very simple producer & comsumer model by threading.Condition

import threading
import time

tmp = 0
g_cond = threading.Condition()

def consumer_thread_func():
    global tmp
    global g_cond
    g_cond.acquire()
    while(True):
        if(tmp > 5):
            tmp -= 1
            print "subthread consumed tmp: %d" % tmp
        else:
            g_cond.wait()
            print "waked up by another thread!"
    g_cond.release()



if __name__ == '__main__':
    t = threading.Thread(target=consumer_thread_func, args=())
    t.setDaemon(True)
    t.start()

    while(True):
        g_cond.acquire()
        if(tmp>=10):
            print "wake up subthread"
            g_cond.notify()
        else:
            tmp += 1
            print "mainthred produced tmp: %d" % tmp
        g_cond.release()
        time.sleep(1)
    t.join()
