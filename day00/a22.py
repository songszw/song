import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容:')
# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=dict2.index'
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
# head={}
# head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
data = {}
data['i']=content
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1493965228879'
data['sign']='1371b00b1571c50710e11c384c0351d9'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='fanyi.webFY_BY_ENTER'
data['typoResult']='true'
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)
target = target['translateResult'][0][0]['tgt']
print('翻译结果是：%s'% target)
