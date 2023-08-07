import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from main import *
import json

class Avitoparse:
    def __init__(self, url:str, items: list, count: int):
        self.url = url
        self.items = items
        self.count = count



    def __setup(self):
        self.driver = uc.Chrome(use_subprocess=False, version_main=115)

    def __geturl(self):
        self.driver.get(self.url)

    def __pagination(self):
        while self.driver.find_elements(By.CSS_SELECTOR, '[aria-label="Следующая страница"]') and self.count > 0:
            self.parse_page()
            self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Следующая страница"]').click()
            self.count -= 1

    def parse_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, '[data-marker="item"]')
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, '[itemprop="name"]').text
            description = title.find_element(By.CSS_SELECTOR, '[class*="item-description"]').find_element(By.CSS_SELECTOR,'[class*="styles-module-size_s"]').text
            url = title.find_element(By.CSS_SELECTOR, '[data-marker="item-title"]').get_attribute('href')
            price = title.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute('content')
            data = {
                'Заголовок': name,
                'Описание': description,
                'Ссылка': url,
                'цена': price

            }
            self.data.append(data)
        self.__save_data()
    def __save_data(self):
        with open('items.json','w',encoding='utf-8') as f:
            json.dump(self.data,f)

    def parse(self):
        self.__setup()
        self.__geturl()
        self.__pagination()


if __name__ == "__main__":
    Avitoparse(url = url, count = 10, items = ['тормозная трубка']).parse()