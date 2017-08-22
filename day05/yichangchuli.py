'''
异常
    1.抓取自己预测的错误
    try:
        code
    except (error1,error2) as e:
        print(e)

    2.抓所有错误
    try :
        code
    except Exception as e:
        print(e)

'''


name = ['alex','jet']
data = {}
try:
    # data['name']
    # name[3]
    a = input('please input your number:')
except (KeyError,IndexError) as e:
    print('错误代码',e)
except Exception as e:
    print('出错了',e)

else:
    print('一切正常')
finally:
    print('不管怎样都会执行')