class Dog:
    def __init__(self,name,sex,age,food='boon',life_value=100):
        self.name = name
        self.sex = sex
        self.age = age
        self.food = food
        self.__live_value = life_value
    def __del__(self):
        print('%s is dead'%self.name)
    def gotshot(self):
        self.__live_value-=10
        print('i got shoot')
    def showInfo(self):
        print('%s infomation: food->%s age->%s blood->%s'%(self.name,self.food,self.age,self.__live_value))
    def wang(self):
        print('%s : this is %s, who are you?'%(self.name,self.name))
    def eat(self):
        print('my name is %s , i\'m eating %s'%(self.name,self.food))
    def fight(self):
        print('get out of there, i will eat you')

d1 = Dog('alex','man',50)
d1.eat()
print(d1.name)
d1.showInfo()
d1.gotshot()
d1.showInfo()
