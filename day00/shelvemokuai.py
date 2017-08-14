import shelve
import datetime
d = shelve.open('shelve_test')
info = {'age':26,'job':'IT'}
name = ['Jet','Hu','Lily']
d['name'] = name
d['info'] = info
d['date'] = datetime.datetime.now()
d.close()
