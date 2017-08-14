class Ssd(str):
    def __new__(cls, string):
        string = string*1.8+32
        return  str.__new__(cls,string)
a = Ssd(32)
print(a)