import time
def bar ():
    time.sleep(1)
    print('this is bar')

def test1(func):
    start = time.time()
    func()
    stop = time.time()
    print('func run time %s' %(stop-start))

test1(bar)