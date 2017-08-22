def talk(self):
    print('alex')

Foo = type('Foo',(),{'a':talk})
f = Foo()
f.a()