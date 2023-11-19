import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from config import config


@pytest.mark.mobile
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Onboarding Process")
@allure.title("Onboarding Screen Functionality Test")
@allure.description(
    "Verifies the onboarding process in the mobile application. The test covers two main steps of the onboarding screen, "
    "ensuring each step displays the correct text and the navigation buttons function as expected."
)
def test_onboarding_screen():
    with allure.step('Verify first step'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Welcome to CoinMarketCap"]')) \
            .should(have.text('Welcome to CoinMarketCap'))
        browser.element((AppiumBy.ID, 'com.coinmarketcap.android:id/onboarding_home')).click()

    with allure.step('Verify second step'):
        browser.element((AppiumBy.ID, 'com.coinmarketcap.android:id/tvTitle')).should(
            have.text('One last thing before we begin…'))
        browser.element((AppiumBy.ID, 'com.coinmarketcap.android:id/btnDone')).click()


@pytest.mark.mobile
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Search Functionality")
@allure.title("Cryptocurrency Search Functionality Test")
@allure.description(
    "Verifies the search functionality in the mobile application. The test involves tapping on the search field, "
    "entering a specific cryptocurrency symbol (e.g., 'BTC'), selecting the first search result, and verifying that "
    "the search results page displays the correct symbol."
)
def test_search(skip_onboarding):
    symbol = 'BTC'
    search_field = browser.element((AppiumBy.ID, 'com.coinmarketcap.android:id/ivSearch'))

    with allure.step(f'Search for Currency {symbol}'):
        search_field.click()
        browser.element((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.coinmarketcap.android:id/searchEditView"]')).send_keys(symbol)

    with allure.step(f'Select First Search Result for {symbol}'):
        browser.element((AppiumBy.XPATH,
                         '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.coinmarketcap.android:id/recyclerView"]/android.widget.RelativeLayout[1]')).click()

    with allure.step('Verify Correct Search Result Page'):
        browser.element((AppiumBy.ID, 'com.coinmarketcap.android:id/barTitle')).should(have.text(symbol))


@pytest.mark.mobile
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Login Functionality")
@allure.title("Mobile App Login Functionality Test")
@allure.description(
    "Verifies the login process in the mobile application. The test includes steps to navigate to the login screen, "
    "enter login credentials, and validate successful login by checking the user's profile information."
)
def test_login(skip_onboarding):
    login = config.cmc_user.login
    password = config.cmc_user.password

    with allure.step("Navigate to Login Screen"):
        profile_avatar = browser.element((AppiumBy.ID, 'com.coinmarketcap.android:id/img_avatar'))

        profile_avatar.click()
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Log in"]')).click()

    with allure.step("Enter Login Credentials"):
        input_login = browser.element((AppiumBy.XPATH,
                                       '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText'))
        input_login.click()
        input_login.send_keys(login)

        input_password = browser.element(
            (AppiumBy.XPATH, '//android.view.View[@content-desc="Password"]/android.widget.EditText'))
        input_password.click()
        input_password.send_keys(password)

    with allure.step("Submit Login Form"):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Log In"]')).click()

    with allure.step("Verify Successful Login"):
        profile_avatar.click()
        browser.element((AppiumBy.ID, 'com.coinmarketcap.android:id/tvUserEMail')).should(have.text(login))
