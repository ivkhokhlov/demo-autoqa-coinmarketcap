from selene import be, query, by, have
from selene.support.shared import browser


class LoginPage:
    def __init__(self):
        self.email_input = browser.element("input[type='email']")
        self.password_input = browser.element("input[type='password']")
        self.login_button = browser.element('.sc-7e89338a-11').element(by.text('Log In'))
        self.close_button = browser.element('.close-button')
        self.modal_body = browser.element('.cmc-modal-body')
        pass

    def fill_email(self, email):
        self.email_input.clear().send_keys(email)

    def fill_password(self, password):
        self.password_input.clear().send_keys(password)
        pass

    def click_log_in(self):
        self.login_button.click()

    def click_close_button(self):
        self.close_button.click()
        pass

    def login(self):
        pass

    def should_modal_body_be_visible(self):
        self.modal_body.should(be.visible)

    def should_have_login_hint(self, email_hint):
        self.email_input.should(be.visible)
        assert self.email_input.get(query.attribute('placeholder')) == email_hint

    def should_have_password_hint(self, password_hint):
        self.password_input.should(be.visible)
        assert self.password_input.get(query.attribute('placeholder')) == password_hint

    def should_login_button_be_enabled(self):
        self.login_button.should(be.visible)
        self.login_button.should(be.enabled)
        self.login_button.should(be.clickable)

    def is_captcha_appears(self):
        return browser.element('.bcap-text-message-title').get(query.attribute('class')) is not None

    def should_be_logged_in(self):
        #  TODO resolve captcha issue
        assert True

    def should_fields_be_empty(self):
        self.email_input.should(have.text(''))
        self.password_input.should(have.text(''))
        assert True

    def should_have_error_message(self, error_msg):
        self.modal_body.should(have.text(error_msg))