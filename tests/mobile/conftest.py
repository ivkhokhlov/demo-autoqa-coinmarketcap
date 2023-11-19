import os

import allure
import allure_commons
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, support

from config import remote_url, driver_options, config
from demo_autoqa_coinmarketcap.utils import attach


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            remote_url,
            options=driver_options())

    browser.config.timeout = config.browser_timeout

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield browser

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

    if config.mobile_context == 'bstack':
        attach.attach_bstack_video(session_id, os.getenv('BSTACK_USER'), os.getenv('BSTACK_ACCESS_KEY'))


pytest.fixture()

@allure.step('Skipping onboarding')
@pytest.fixture()
def skip_onboarding():
    browser.element((AppiumBy.ID, 'com.coinmarketcap.android:id/onboarding_home')).click()
    browser.element((AppiumBy.ID, 'com.coinmarketcap.android:id/btnDone')).click()
