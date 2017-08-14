import time
def cousumer(name):
    print('%s is ready to eat the baozi'% name)
    while True:
        baozi = yield
        print('baozi %s is comming, %s eat it' %(baozi,name))

def producer(cook):
    A = cousumer('A')
    B = cousumer('B')
    A.__next__()
    B.__next__()
    print('%s is ready to cook the baozi' % cook)
    for i in range(10):
        time.sleep(2)
        print('%s already cooked a baozi' % cook)
        A.send(i)
        B.send(i)

producer('Jet')
