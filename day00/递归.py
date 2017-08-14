def calc(n):
    print(n)
    if int(n/2) >0:
        return calc(int(n/2))
    print('n最后的值是==>',n)
calc(10)