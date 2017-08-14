from bs4 import BeautifulSoup
import requests
url='https://songszw.github.io/'
my_data = requests.get(url)
soup = BeautifulSoup(my_data.text,'lxml')
print(soup)
titles = soup.select('div.itemsRight > h2')
contents = soup.select('div.itemsRight > p')
imgs = soup.select('div.itemsLeft > a > img')
for title,content,img in zip(titles,contents,imgs):
    data={
        'title':title.get_text(),
        'content':list(content.stripped_strings),
        'img':img.get('src')
    }
    print(data)
