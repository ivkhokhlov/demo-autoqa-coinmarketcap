import allure
import pytest
from allure_commons.types import Severity

from config import config
from demo_autoqa_coinmarketcap.pages.manager import cmc_ui


@pytest.mark.ui
@pytest.mark.smoke
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'master_klinka')
@allure.story("Login Functionality")
@allure.title("Login Functionality from Main Page")
@allure.description(
    "Tests the login process from the main page of the application. It includes steps like opening the main page, "
    "clicking the login button, filling in credentials, and verifying successful login. The test also handles "
    "the potential appearance of a captcha."
)
def test_login_from_main_page():
    with allure.step("Open Main Page"):
        cmc_ui.main_page.open()
    with allure.step("Click on Login Button"):
        cmc_ui.main_page.click_login()

    with allure.step("Verify Login Modal Visibility and Hint Texts"):
        cmc_ui.login_page.should_modal_body_be_visible()
        cmc_ui.login_page.should_have_login_hint('Enter your email address...')
        cmc_ui.login_page.should_have_password_hint('Enter your password...')

    with allure.step("Fill in Email and Password"):
        cmc_ui.login_page.fill_email(config.cmc_user.login)
        cmc_ui.login_page.fill_password(config.cmc_user.password)

    with allure.step("Click on Log In Button"):
        cmc_ui.login_page.click_log_in()

    with allure.step("Handle Captcha if Appears"):
        if cmc_ui.login_page.is_captcha_appears():
            pytest.skip("Captcha Issue")
    with allure.step("Verify Successful Login"):
        cmc_ui.login_page.should_be_logged_in()


@pytest.mark.ui
@pytest.mark.smoke
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'master_klinka')
@allure.story("Login Functionality")
@allure.title("Login Functionality from Currency Page")
@allure.description(
    "Verifies the login process when initiated from the currency page. This test covers opening the currency page, "
    "clicking the login button, inputting credentials, and confirming a successful login. Additionally, the test "
    "accounts for a potential captcha challenge."
)
def test_login_from_currency_page():
    with allure.step("Open Currency Page"):
        cmc_ui.currency_page.open_default()

    with allure.step("Click on Login Button"):
        cmc_ui.main_page.click_login()

    with allure.step("Verify Login Modal Elements"):
        cmc_ui.login_page.should_modal_body_be_visible()
        cmc_ui.login_page.should_have_login_hint('Enter your email address...')
        cmc_ui.login_page.should_have_password_hint('Enter your password...')

    with allure.step("Enter Login Credentials"):
        cmc_ui.login_page.fill_email(config.cmc_user.login)
        cmc_ui.login_page.fill_password(config.cmc_user.password)

    with allure.step("Attempt to Log In"):
        cmc_ui.login_page.click_log_in()

    with allure.step("Handle Captcha Verification"):
        if cmc_ui.login_page.is_captcha_appears():
            pytest.skip("Captcha Issue")

    with allure.step("Check if Log In was successful"):
        cmc_ui.login_page.should_be_logged_in()


@pytest.mark.ui
@pytest.mark.regress
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Login Functionality")
@allure.title("Login with Invalid Username")
@allure.description(
    "Tests the login process using an invalid username. This test involves opening the default currency page, "
    "triggering the login modal, filling in an invalid email address with a valid password.")
def test_login_invalid_user_name():
    with allure.step("Open Currency Page"):
        cmc_ui.currency_page.open_default()

    with allure.step("Initiate Login Process"):
        cmc_ui.main_page.click_login()

    with allure.step("Check Login Modal Visibility and Input Hints"):
        cmc_ui.login_page.should_modal_body_be_visible()
        cmc_ui.login_page.should_have_login_hint('Enter your email address...')
        cmc_ui.login_page.should_have_password_hint('Enter your password...')

    with allure.step("Input Invalid Email and Valid Password"):
        cmc_ui.login_page.fill_email("invalid_email")
        cmc_ui.login_page.fill_password(config.cmc_user.password)

    with allure.step("Attempt to Log In"):
        cmc_ui.login_page.click_log_in()

    with allure.step("Verify Error Message for Invalid Username"):
        cmc_ui.login_page.should_have_error_message(
            'The email you entered is not in the correct format. Please check.')


@pytest.mark.ui
@pytest.mark.regress
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Login Functionality")
@allure.title("Login with Invalid Password")
@allure.description(
    "This test validates the login process using a valid username but an invalid password. It includes steps for "
    "opening the default currency page, initiating the login process, entering credentials, and verifying the "
    "appropriate error message for the incorrect password."
)
def test_login_invalid_password():
    with allure.step("Open Currency Page"):
        cmc_ui.currency_page.open_default()

    with allure.step("Initiate Login Process"):
        cmc_ui.main_page.click_login()

    with allure.step("Verify Login Modal Elements"):
        cmc_ui.login_page.should_modal_body_be_visible()
        cmc_ui.login_page.should_have_login_hint('Enter your email address...')
        cmc_ui.login_page.should_have_password_hint('Enter your password...')

    with allure.step("Enter Valid Email and Invalid Password"):
        cmc_ui.login_page.fill_email(config.cmc_user.login)
        cmc_ui.login_page.fill_password("random_password123!")

    with allure.step("Attempt to Log In"):
        cmc_ui.login_page.click_log_in()

    with allure.step("Handle Captcha Verification"):
        if cmc_ui.login_page.is_captcha_appears():
            pytest.skip("Captcha Issue")
    with allure.step("Confirm Error Message for Invalid Password"):
        cmc_ui.login_page.should_have_error_message('Your email and password does not match. Please try again')


@pytest.mark.ui
@pytest.mark.regress
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'username')
@allure.story("Login Functionality")
@allure.title("Clear Fields on Login Modal Close")
@allure.description(
    "Verifies that all input fields in the login modal are cleared when the modal is closed and reopened. "
    "The test covers opening the main page, triggering the login modal, filling in credentials, closing the modal, "
    "reopening it, and checking that the fields are empty."
)
def test_fields_cleared_on_modal_close():
    with allure.step("Open Main Page"):
        cmc_ui.main_page.open()

    with allure.step("Open Login Modal"):
        cmc_ui.main_page.click_login()

    with allure.step("Fill in Email and Password"):
        cmc_ui.login_page.fill_email(config.cmc_user.login)
        cmc_ui.login_page.fill_password(config.cmc_user.password)

    with allure.step("Close Login Modal"):
        cmc_ui.login_page.click_close_button()

    with allure.step("Reopen Login Modal"):
        cmc_ui.main_page.click_login()

    with allure.step("Verify Fields Are Cleared"):
        cmc_ui.login_page.should_fields_be_empty()
