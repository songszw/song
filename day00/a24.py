import urllib.request
import os

def urlOpen(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html
def getPage(url):
    html = urlOpen(url).decode('utf-8')
    a = html.find('current-comment-page')+23
    b = html.find(']',a)
    return html[a:b]

def findImg(url):
    html=urlOpen(url).decode('utf-8')
    imgAddres = []
    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            imgAddres.append(html[a + 9:b + 4])
        else:
            b = a + 9
        a = html.find('img src=', b)
    return imgAddres


def saveImg(folder,imgAddres):
   for each in imgAddres:
       filename = each.split('/')[-1]
       with open(filename,'wb') as f:
           img = urlOpen(each)
           f.write(img)



def download_mm(folder = 'heihei',page=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    pageNum =int(getPage(url))
    for i in range(pageNum):
        pageNum-=i
        pageUrl = url+'page-'+str(pageNum)+'#comments'
        imgAddres = findImg (pageUrl)
        saveImg(folder,imgAddres)
if __name__ == '__main__':
    download_mm()