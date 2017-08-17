class People(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('%s is eating'%self.name)

    def talk(self):
        print('%s id talking'% self.name)
    def sleep(self):
        print('%s id sleep'% self.name)
class Relation(object):
    def make_friends(self,friend):
        print('%s is making friend with %s'%(self.name,friend.name))

class Man(People,Relation):
    def __init__(self,name,age,money):
        # People.__init__(self,name,age)
        super(Man,self).__init__(name,age)
        self.money = money
        print('When %s was born,%s got %s money '%(self.name,self.name,self.money))
    def piao(self):
        print('%s is piao...'% self.name)
    def talk(self):
        People.sleep(self)
        print('%s is talking with his self'%self.name)

class Women(People):
    def buy(self):
        print('%s is shopping'%self.name)
m1 = Man('Alex',23,1000)
# print(m1.name)
# m1.talk()
# m1.piao()
# m2 = Man('jet',26,2000)
# m2.talk()

g1 = Women('lalala',40)
# g1.buy()
m1.make_friends(g1)