# create a simple thread pool

import Queue, threading, sys
import time


class _Thread(threading.Thread):
    def __init__(self, workQueue, resultQueue, timeout=1, **kwargs):
        super(_Thread, self).__init__(kwargs= kwargs)
        self.setDaemon(True)
        self.timeout = timeout
        self.workQueue = workQueue
        self.resultQueue = resultQueue

    def run(self):
        while True:
            try :
                callable_func, args, kwargs = self.workQueue.get(timeout= self.timeout)
                res = callable_func(*args, **kwargs)
                print res + "  computed by thread:  " + threading.currentThread().getName() + " | "
                self.resultQueue.put(res + "  |  " + threading.currentThread().getName())
            except Queue.Empty:
                break
            except :
                print sys.exc_info()
                raise


class Thread_Pool(object):
    def __init__(self, num_of_threads=2):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.threads = []
        self.__createThreadPool(num_of_threads)

    def __createThreadPool(self, num_of_threads):
        for i in range(num_of_threads):
            thread = _Thread(self.workQueue, self.resultQueue)
            self.threads.append(thread)

    def add_job(self, callable_func, *args, **kwargs):
        self.workQueue.put((callable_func, args, kwargs))


    def start(self):
        for thread in self.threads:
            thread.start()

    def wait_thread_pool_end(self):
        while self.threads:
            thread = self.threads.pop()
            if thread.isAlive():
                thread.join()


def test_job(id, timeout=0.1):
    time.sleep(0.1)
    return str(id)

def test():
    print "start thread pool testing!"
    tp = Thread_Pool(3)
    for i in range(100):
        tp.add_job(test_job, i, i)
    tp.start()
    tp.wait_thread_pool_end()

    print "resultQueue length is %d" % tp.resultQueue.qsize()

    while tp.resultQueue.qsize():
        print tp.resultQueue.get()

    # print str(tp.resultQueue)

    print "end thread pool test!"


if __name__ == "__main__":
    test()

