import pytest
from selene import browser, have, be #browser, have, be  - модули


def test_complete_todo():
    browser.open('/')

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.size(3))
