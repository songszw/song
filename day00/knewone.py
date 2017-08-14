from bs4 import BeautifulSoup
import requests
import time
url = 'https://knewone.com/discover?page=5'
def get_page(url,data=None):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    titles=soup.select('section.content > h4 > a')
    imgs = soup.select(' header.cover > a > img')
    links = soup.select('section.content > h4 > a')
    if data==None:
        for img,title,link in zip(imgs,titles,links):
            data={
                'img':img.get('src'),
                'title':title.get('title'),
                'link':link.get('href')
            }
            print(data)

def get_more_page(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)

get_more_page(1,10)