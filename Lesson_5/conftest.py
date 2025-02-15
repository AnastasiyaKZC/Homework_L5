#фикстура. Влияет на всю папку, в которой лежит (в корне проекта тоже будет работать)
#В conftest чаще пишут технические фикстуры (то, что не описывает тестовую логику)


import driver
import pytest
import selene
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs' #для переиспользования base_URL пишем '/'

    # запускает браузер в невидимом режиме - быстрее выполняется тест в headless-режиме
    # driver_options = webdriver.ChromeOptions
    # driver_options.add_argument('--headless=new')
    # browser.config.driver_options = driver_options

    # selene.browser.config.type_by_js = True - вводит текст быстро а не по одному символу
    #селен ждет выполнения теста (ожидание элемента) по умолчанию 4 секунды, это можно конфигурировать для скорости выполнения:
    # browser.config.timeout = 2.0

    yield

    browser.quit()