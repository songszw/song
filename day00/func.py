# import time
#
# def logger():
#     time_format = '%Y-%m-%d %X'
#     time_current = time.strftime(time_format)
#     with open('song003','a+') as f:
#         f.write('%s end action\n' % time_current)
#
# def fun1():
#     print('this is func1')
#     logger()
# def fun2():
#     print('this is func2')
#     logger()
# def fun3():
#     print('this is func3')
#     logger()
#
# fun1()
# fun2()
# fun3()
'''
**kwargs  把关键字参数转换成字典的方式
'''
def test1(name,**kwargs):
    print(name)
    print(kwargs)
    print(kwargs['age'])
    print(kwargs['salary'])
test1('song',age = 26,salary = 15000)