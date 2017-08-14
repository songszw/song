class C:
    def __init__(self,*args):
        if not args:
            print('没有传入参数')
        else:
            print('传入了%d 个参数，分别是：'% len(args), end='')
            for each in args:
                print(each,end='')


a = C()
b = C(1,5,8)
