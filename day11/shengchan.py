import threading,time
import queue
q = queue.Queue(maxsize=10)
def Producer(name):
    count = 1
    while True:
        q.put('骨头%s'%count)
        print('生产了骨头',count)
        count+=1
        time.sleep(0.1)

def Consumer(name):
    while q.qsize()>=0:
        print('%s get %s and eat it'%(name,q.get()))
        time.sleep(1)



p = threading.Thread(target=Producer,args=('Ales',))
c = threading.Thread(target=Consumer,args=('Zhangyang',))
c2 = threading.Thread(target=Consumer,args=('yuliuyang',))
p.start()
c.start()
c2.start()
