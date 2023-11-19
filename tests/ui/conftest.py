import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import config
from demo_autoqa_coinmarketcap.utils import attach


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default=config.default_browser_version
    )
    parser.addoption(
        '--browser_name',
        default=config.default_browser_name
    )

@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')
    browser_name = request.config.getoption('--browser_name')

    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = config.selenoid_user.login
    password = config.selenoid_user.password
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    browser.config.browser_name = browser_name
    browser.config.window_width = 1366
    browser.config.window_height = 768
    browser.config.timeout = config.browser_timeout
    browser.config.base_url = 'https://coinmarketcap.com'

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
