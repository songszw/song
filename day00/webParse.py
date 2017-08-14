from bs4 import BeautifulSoup
import requests
import time
url = 'https://www.tripadvisor.cn/Attractions-g298507-Activities-oa30-St_Petersburg_Northwestern_District.html#ATTRACTION_LIST'
urls=['https://www.tripadvisor.cn/Attractions-g298507-Activities-oa{}-St_Petersburg_Northwestern_District.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,900,30)]



def getContent(url,data=None):
    time.sleep(4)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('div.listing_title > a[target="_blank"]')
    imgs = soup.select('img[width="180"]')
    cates = soup.select('div.p13n_reasoning_v2')
    for title, img, cate in zip(titles, imgs, cates):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings)
        }
        print(data)

# getContent(url)
# print(urls)
for single_url in urls:
    getContent(single_url)