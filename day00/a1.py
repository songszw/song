class Birds:
    def fly(self):
        print('i`m a bird, i can fly')
    def eat(self):
        print('i`m hungury')
class Penguin(Birds):
    def fly(self):
        print('i`m penguin, i`m a kind of birds, but i can`t fly')

a = Birds()
b = Penguin()
a.fly()
b.fly()
a.eat()
b.eat()
