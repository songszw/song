class Dog(object):
    '''
    这个类是描述狗这个对象的
    '''
    def __init__(self,name):
        self.name = name
        self.__food = None


d = Dog
print(d.__doc__)
