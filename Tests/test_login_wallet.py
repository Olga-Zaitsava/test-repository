from Steps.login_steps import login_to_wallet
from selenium.webdriver import Chrome

import pytest

@pytest.fixture(scope='function')
def open_wallet():
    browser = Chrome('/Users/olga/Documents/chromedriver/chromedriver')
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get("https://wallet.neo.getcurrencies.com")

def test_login(open_wallet):
    login_to_wallet(open_wallet)







