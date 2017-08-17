class Dog:
    def __init__(self,name,sex,age,food='boon'):
        self.name = name
        self.sex = sex
        self.age = age
        self.food = food
    def wang(self):
        print('%s : this is %s, who are you?'%(self.name,self.name))
    def eat(self):
        print('my name is %s , i\'m eating %s'%(self.name,self.food))
    def fight(self):
        print('get out of there, i will eat you')

d1 = Dog('alex','man',50)
d2 = Dog('zhangyang','woman',23)
print(d1.name)
d1.wang()
d2.food = 'noodles'
d2.eat()
d1.eat()