import threading
class MyThreading(threading.Thread):
    def __init__(self,n):
        super(MyThreading,self).__init__()
        self.n = n

    def run(self):
        print('running task',self.n)

t1 = MyThreading('y1')
t2 = MyThreading('y2')
t1.run()
t2.run()