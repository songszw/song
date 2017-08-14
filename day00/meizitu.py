from bs4 import BeautifulSoup
import requests
import urllib.request
import time
img_url = []
# url = 'http://jandan.net/ooxx/page-177#comments'
url = ['http://jandan.net/ooxx/page-{}#comments'.format(str(i)) for i in range(1,10)]
folder_path = 'C:/Users/songs/Desktop/python/picpa/meizitu/'
def getContent(url,data=None):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    imgs = soup.select('div.text > p > img')

    for img in imgs:
        link = 'http:' + img.get('src')
        img_url.append(link)

for a in url:
    time.sleep(2)
    getContent(a)

for item in img_url:
    time.sleep(2)
    print(img_url)
    urllib.request.urlretrieve(item,folder_path+item[-10:])


