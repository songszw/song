# all 如果里面内容都为真就返回true，0是false
# print(all([1,-5,3]))
# any 只要有一个为真，就是true， 同样0为false
# print(any([1]))
# ascii 将中文的ascii码显示出来,并且将格式转化成字符串
# print(ascii([1,2,'你好']))
# bin 将10进制转成2进制
# print(bin(255))
# bool 布尔值
# bytearray 可修改的二进制字节格式
a = bytes('abcde',encoding='utf-8')
print(a.capitalize(),a)
b = bytearray('cdefg',encoding='utf-8')
b[0]=102
print(b)