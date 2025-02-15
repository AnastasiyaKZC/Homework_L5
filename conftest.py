#фикстура. сюда вынесено все что касается настройки и управления браузером
import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs' #для переиспользования base_URL пишем '/'

    yield

    browser.quit()