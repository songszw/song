import shelve
import datetime
d = shelve.open('shelve_test')
a = d.get('name')
b = d.get('info')
c = d.get('date')
print(a,b,c)
print(a[1])