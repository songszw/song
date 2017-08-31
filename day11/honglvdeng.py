import time

import threading
event = threading.Event()
def lighter():
    count = 0
    event.set()
    while True:
        if count>5 and count <=10:
            event.clear()
            print('\033[41;1mred light is on....\033[0m')
        elif count>10:
            event.set()
            count = 0
        else:
            print('\033[42;1mgreen light is on...\033[0m')
        time.sleep(1)
        count+=1
def car(name):
    while True:
        if event.is_set():
            print('car[%s] is running...'%name)
            time.sleep(1)
        else:
            print('car [%s] sees red light, is waiting... '%name)
            event.wait()
            print('\033[34;1m[%s] green light is on , start going\033[0m '%name)

light = threading.Thread(target=lighter)
light.start()
car1 = threading.Thread(target=car,args=('Tesla',))
car1.start()