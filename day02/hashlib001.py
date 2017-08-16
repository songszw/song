import hashlib
m = hashlib.md5()
m.update(b'Hello')
print(m.hexdigest())
m.update(b'it\' me')
print(m.hexdigest())
m.update(b'It\'s been a long time not see')
print(m.hexdigest())

s1 = hashlib.sha1()
s1.update(b'hei')
print(s1.hexdigest())

m2 = hashlib.md5()
m2.update('天王盖地虎'.encode(encoding='utf-8'))
print(m2.hexdigest())
import hmac
h = hmac.new(b'hello','小鸡炖蘑菇'.encode(encoding='utf-8'))
print(h.hexdigest())