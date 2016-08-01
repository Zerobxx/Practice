import threading
import time

g_event = threading.Event()

def func():
    global g_event

    while True:
        # if(g_event.isSet()):
        #     g_event.clear()
        print 'start event wait'
        g_event.wait()
        print 'wake up by event.set()'
        g_event.clear()
        print 'clear set'


if __name__ == "__main__":
    t = threading.Thread(target=func, args=())
    t.setDaemon(True)
    t.start()

    while True:
        time.sleep(1)
        print 'wake up subthread'
        g_event.set()



    t.join()
