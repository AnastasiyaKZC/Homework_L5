import pytest
from selene import browser, have, be #browser, have, be  - модули

@pytest.fixture()
def open_app():
    browser.open('/')

def test_complete_todo(open_app):
    #browser.open('/') #по умолчанию используется браузер Chrome, иное можно указать в конфигурации browser.config.driver_name = 'firefox' (вынесла в фикстуру)

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    # browser.all('#todo-list>li').with_(timeout=browser.config * 2).should(have.size(3)) #для этой команды таймаут будет вдвое больше чем указанный в фикстуре
    # browser.all('#todo-list>li').first.should(have.exact_text('a'))
    # browser.all('#todo-list>li').second.should(have.exact_text('b'))
    # browser.all('#todo-list>li')[2].should(have.exact_text('c'))

    browser.all('#todo-list>li')[2].should(have.exact_texts('a', 'b', 'c')) - #эта проверка заменяет предыдущие 4 - есть все три эти элемента и именно в таком порядке





    # в селене можно выполнить некоторые команды JS - пример:  browser.element('#save').perform(command.js.click)

