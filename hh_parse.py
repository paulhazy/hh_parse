from bs4 import BeautifulSoup
import requests

url = 'https://samara.hh.ru/search/vacancy?area=78&st=searchVacancy&text=devops'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/79.0.3945.117 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
                          'Connection': 'keep-alive'}

def code(url):
    stat = requests.get(url, headers=headers)
    return stat


def get_html_code(url, headers):
    html = code(url)
    if html.status_code == 200:
        print('good code, keep going\n')
        ses = requests.Session()
        req = ses.get(url, headers=headers)
        soup = BeautifulSoup(req.content, "html.parser")
        get_div = soup.find_all("a", class_="bloko-link HH-LinkModifier")

        for i in get_div:

            print(i)
    else:
        print('fucked up!')
get_html_code(url, headers)
