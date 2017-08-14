class C:
    def __init__(self,size = 10):
        self.size = size

    def getXSize(self):
        return  self.size

    def setXSize(self,value):
        self.size = value

    def delXSize(self):
        del  self.size

    x = property(getXSize, setXSize, delXSize)


c = C()
print(c.x)
c.x = 15
print(c.x)
del c.x
print(c.x)
