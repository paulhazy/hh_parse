from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

url = 'https://samara.hh.ru/search/vacancy?area=78&st=searchVacancy&text=devops&fromSearch=true'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/79.0.3945.117 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
                          'Connection': 'keep-alive'}


def get_code(url):
    stat = requests.get(url, headers=headers)
    return stat

def get_hrefs(url, headers):
    html = get_code(url)
    if html.status_code == 200:
        print('good code, keep going\n')
        ses = requests.Session()
        req = ses.get(url, headers=headers)
        soup = BeautifulSoup(req.content, "html.parser")
        get_div = soup.find_all("a", class_="bloko-link HH-LinkModifier")
        links = []
        for i in get_div:
            link = i['href']
            links.append(link)
        return links
    else:
        return 'fucked up!'
#print(get_hrefs(url, headers))
# use print for debug
links=get_hrefs(url, headers)

def get_vacancy(url, headers):
    get_html = get_code(url)
    if get_html.status_code == 200:
        ses = requests.get(url, headers=headers)
        soup = BeautifulSoup(ses.content, "html.parser")
        vacancy = soup.find_all("div", class_='g-user-content')
        #result = []
        for i in vacancy:
            #result.append()
            return i.get_text('\n', strip=True)
    else:
        return 'you fucked up!'

#цикл по каждой ссылке в списке
for urls in links:
    print(get_vacancy(urls, headers))