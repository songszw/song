f = open('song001','r',encoding='utf-8')
'''
for index,line in enumerate(f.readlines()):

    if index == 9:
        print('-------这是第十行---------')
        continue
    print(line.strip())

couont = 0
for line in f:
    if couont == 10:
        print('-------我是第十行----------')
        couont+=1
        continue
    print(line.strip())
    couont+=1
print(f.tell())
print(f.seek(0))
print(f.encoding)
print(f.buffer)
'''
f_new = open('song002','w',encoding='utf-8')
for line in f:
    if 'How I wondered where they\'d gone' in line:
        line = line.replace('How I wondered where they\'d gone','宋智文万岁万岁万万岁')
    f_new.write(line)

f.close()
f_new.close()
