import time
class JetException(Exception):
    def __init__(self,msg):
        self.message = msg
n = True
k=0
while n:
    try:
        k+=1
        print(k)
        time.sleep(2)
        if k>10 :
            n = False
            raise JetException('what the fuck')
    except JetException as e:
        print(e)











