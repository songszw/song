class Turtle:
    def __init__(self,x):
        self.num = x
class Fish:
    def __init__(self,x):
        self.num = x
class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.Fish = Fish(y)

    def print_num(self):
        print('水池里共有 %d 乌龟和 %d 条鱼'%(self.turtle.num,self.Fish.num))

pool = Pool(3,100)
pool.print_num()