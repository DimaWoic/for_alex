import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class SafeParser():

    def __init__(self):
        url = 'http://surgut.snert.ru/category/seyfy'
        user_agent = UserAgent()
        headers = {'User-Agent': user_agent.chrome}
        page_get = requests.get(url, headers=headers)
        if page_get.status_code == 200:
            self.page_html = page_get.text
            print(page_get.text)
        else:
            print('Ошибка соединения ' + str(page_get.status_code))


page = SafeParser()
p = page.page_html
print(p)