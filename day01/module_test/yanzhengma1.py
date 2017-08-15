import random
num = ''
for i in range(4):
    a = random.randrange(0,5)
    print(a)
    if a == i:
        a = random.randint(0,9)
    else:
        a = chr(random.randint(65,90))
    num+=str(a)

print(num)