class Dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod
    def eat(self,food):
        print('%s is eating %s'%(self.name,food))

d = Dog('张杨')
d.eat(d,'包子')
