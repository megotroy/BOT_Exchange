import requests
from bs4 import BeautifulSoup
import lxml
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random
URL = "https://mainfin.ru/currency/moskva"
HEADERS = {
    'user_agent': user_agent
}

def set_url(url):
    r = requests.get(url, params=None, headers=HEADERS)
    return r.content
def set_html(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find('table', class_='table table-bordered table-exchange')
    items = items.find('td', class_="info")
    name = []
    for item in items:
        name.append(item)
    html = f'{name[0][:5]}'
    return html

def main():
    html = set_url(url=URL)
    cur = set_html(html)
    return cur