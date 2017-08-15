import random
num = ''
for i in range(4):
    current = random.randrange(0,5)
    if current == i:
        current = random.randint(0,9)
    else:
        current =chr(random.randint(65,90))
    num += str(current)

print(num)
