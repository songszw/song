class Animal(object):
    def __index__(self,name):
        self.name = name
    #
    def talk(self):
        pass
        # raise NotImplementedError('Subclass')
    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print('喵')

class Dog(Animal):
    def talk(self):
        print('汪汪')
d1 = Dog()
c1 = Cat()


Animal.animal_talk(c1)
Animal.animal_talk(d1)