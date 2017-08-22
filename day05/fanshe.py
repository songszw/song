'''
反射
    hasattr(obj,name_str)
        判断一个对象obj里面是否存在字符串name_str所对应的方法
    getattr(obj,name_str)
        根据字符串name_str去获取obj对象里对应的方法的内存地址

'''
class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print('%s is eating %s'% (self.name,food))

def bulk(self):
    print('%s is yelling ...'% self.name)

d1 = Dog('alex')
choice = input('>>:').strip()

if hasattr(d1,choice):
    attr = getattr(d1,choice)
    attr('大便')
else:
    # setattr(d1,choice,bulk)
    # d1.talk(d1)
    setattr(d1,choice,22)
    print(getattr(d1,choice))









