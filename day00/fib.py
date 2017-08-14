# def fib(max):
#     n,a,b = 0,0,1
#     while n<max:
#         print(b)
#         a,b = b,a+b
#         n=n+1
#     return 'done'
# fib(10)
# print(fib(10))
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        t = (b,a+b)
        a=t[0]
        b=t[1]
        n=n+1
f = fib(10)
a = True
while a :
    try:
        print(f.__next__())
    except StopIteration as e:
        print('Generator return value:',e.value)
        a = False