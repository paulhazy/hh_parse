from bs4 import BeautifulSoup
import requests

url = 'https://samara.hh.ru/vacancy/37080613?query=devops'
headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
                        'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
                        'Connection': 'keep-alive'
}

def get_http_code(url):
    requ = requests.get(url, headers=headers)
    return requ

def get_vacancy(url, headers):
    get_html = get_http_code(url)
    if get_html.status_code == 200:
        ses = requests.get(url, headers=headers)
        soup = BeautifulSoup(ses.content, "html.parser")
        vacancy = soup.find_all("div", class_='g-user-content')
#       result = []
        for i in vacancy:
#           result.append()
            return i.get_text('\n', strip=True)
    else:
        print('you fucked up!')


print(get_vacancy(url, headers))
