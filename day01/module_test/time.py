'''
标准库中有两个模块，time和datetime
一般情况下时间格式分为
1、格式化字符串形式
    2017-08-02 14:25:01
2、时间戳
    time.time()
    从1970年1月1日0点到当前时间的秒数
3、struct_time 元组的方式表示时间，共有9个元素
    
'''
import time
x = time.localtime()

