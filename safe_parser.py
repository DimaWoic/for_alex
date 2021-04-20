import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from os import getcwd
import time
from selenium.webdriver.support.ui import WebDriverWait

class SafeParser():

    def __init__(self):
        self.url_safe = 'http://surgut.snert.ru/category/seyfy'   #url на сейфы
        self.url_wardr = 'http://surgut.snert.ru/category/metallicheskie-shkafy/'   #url на металлические шкафы
        path_to_gecko = getcwd() + '/geckodriver'
        options = webdriver.FirefoxOptions()
        options.headless = False
        self.driver = webdriver.Firefox(executable_path=path_to_gecko, options=options)
        user_agent = UserAgent()
        headers = {'User-Agent': user_agent.chrome}
        page_get_safe = requests.get(self.url_safe, headers=headers)
        if page_get_safe.status_code == 200:
            print("Подключение установлено")
        else:
            print('Ошибка соединения ' + str(page_get_safe.status_code))

    def get_products_safe(self):
        self.driver.get(self.url_safe)
        elem_num_prod = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/div[3]/div[1]/div[2]/a[4]')
        elem_num_prod.click()
        page_href = 'http://surgut.snert.ru/category/seyfy/?page='
        #last_page = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/div[3]/div[2]/ul/li[12]')
        pagination = self.driver.find_element_by_class_name('prd-list-pagination')
        print(pagination.text)
        self.driver.close()


        """
    def get_safe_product_list(self):
        product_list_ul = self.page_html_safe.find('ul', class_='product-list list')
        self.product_list = product_list_ul.findAll('li')
        return self.product_list
        """

parser = SafeParser()
parser.get_products_safe()
