import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class SafeParser():

    def __init__(self):
        url_safe = 'http://surgut.snert.ru/category/seyfy'   #url на сейфы
        url_wardr = 'http://surgut.snert.ru/category/metallicheskie-shkafy/'   #url на металлические шкафы
        user_agent = UserAgent()
        headers = {'User-Agent': user_agent.chrome}
        page_get_safe = requests.get(url_safe, headers=headers)
        page_get_wardr = requests.get(url_wardr, headers=headers)
        if page_get_safe.status_code == 200:
            self.page_html_safe = BeautifulSoup(page_get_safe.text, 'html.parser')   #хранит страницу со списком товаров из категории сейфы
            self.page_html_wardr = BeautifulSoup(page_get_wardr.text, 'html.parser') #хранит страницу со списком товаров из категории металлические шкафы
        else:
            print('Ошибка соединения ' + str(page_get_safe.status_code))

    def get_safe_product_list(self):
        product_list_ul = self.page_html_safe.find('ul', class_='product-list list')
        self.product_list = product_list_ul.findAll('li')
        return self.product_list

