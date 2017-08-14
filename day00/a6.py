class Nstr(str):
    def __sub__(self, other):
        return  self.replace(other,'')

a = Nstr('I Love Fish.com!iiiiiiiiiiiiiiii')
b = Nstr('i')
print(a-b)