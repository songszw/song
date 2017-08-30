import threading
import time


class MyThreading(threading.Thread):
    def __init__(self,n):
        super(MyThreading,self).__init__()
        self.n = n

    def run(self):
        print('running taskm',self.n)

t1 = MyThreading('t1')
t2 = MyThreading('t2')
t1.start()
t2.start()