a = [1,2,3,4,5,6,7]
b = ['a','b','c','d','e','f']
c = []
for i in zip(a,b):
    c.append(i)

print(c)
print(c[0])