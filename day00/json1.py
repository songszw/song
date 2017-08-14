import json
info = {
    'name':'jet',
    'age':26
}
f = open('song004','w')
f.write(json.dumps(info))
f.close()
