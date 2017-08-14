import requests
from bs4 import BeautifulSoup
import urllib.request
url='http://jandan.net/ooxx/page-148#comments'
source_code = requests.get(url)
# plain_text = source_code.text
soup = BeautifulSoup(source_code.text,'lxml')
imgs = soup.select('div.text > p > img')
download_links = []
folder_path = 'C://Users/songs/Desktop/python/picpa/'

for img in imgs:
    link = 'http:'+img.get('src')
    download_links.append(link)

for item in download_links:
    urllib.request.urlretrieve(item,folder_path+item[-10:])
print(download_links)