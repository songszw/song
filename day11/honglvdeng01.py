import threading
import time
event = threading.Event()
def lights():
    count = 0
    event.set()
    while True:
        if count>5 and count<=10:
            event.clear()
            print('\033[41;1mred ligit is on...\033[0m')
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
            print('[%s] is running..'%name)
            time.sleep(1)
        else:
            print('[%s] see the light is turning red,waiting...'%name)
            event.wait()
            print('\033[34;1m[%s] see the light is turning green,start going...\033[0m'%name)

light = threading.Thread(target=lights)
light.start()
car1 = threading.Thread(target=car,args=('Tesla',))
car1.start()