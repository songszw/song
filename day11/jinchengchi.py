from multiprocessing import Process,Pool,freeze_support
import time,os
freeze_support()

def Foo(i):
    time.sleep(1)
    print('in process ',os.getpgid())
    return i+100

def Bar(arg):
    print('-->exec done:',arg)

if __name__=='__main':  #为了区分是不是自己主动执行的脚本
    freeze_support()
    pool = Pool(5)
    for i in range(10):
        pool.apply(func=Foo,args=(i,))
    print('end')
    pool.close()
    # pool.join()
