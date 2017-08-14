import json
f = open('song004','r')
b = json.loads(f.read())
f.close()
print(b)
print(b['age'])