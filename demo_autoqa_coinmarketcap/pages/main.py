import allure
from selene import by, be, have
from selene.support.shared import browser


class MainPage:
    def __init__(self):
        self.search_input = browser.element('.sc-e20acb0c-1')
        self.search_tippy_content = browser.element('.tippy-content')
        self.cmc_table = browser.element('.cmc-table')

    @allure.step('Open main page')
    def open(self):
        browser.open('/')

    def click_login(self):
        browser.element(by.text('Log In')).click()

    def click_search(self):
        self.search_input.click()

    def click_first_tippy_result(self):
        self.search_tippy_content.element('a').click()

    def type_desktop_input_search(self, text_to_search):
        browser.element('.desktop-input').send_keys(text_to_search)

    def click_on_first_row(self):
        self.cmc_table.element('a').click()

    def click_on_row_by_symbol(self, symbol):
        self.cmc_table.element(f"//tr[.//p[contains(text(), '{symbol}')]]").click()

    def should_tabs_be_on_page(self, tab_names: list):
        for tab_name in tab_names:
            browser.element('.scroll-child').should(have.text(tab_name))
            browser.element('.scroll-child').element(by.xpath("//button[contains(text(), 'Telegram Bot')]")).should(
                be.visible)

    def should_tippy_content_have_text(self, text_to_match):
        self.search_tippy_content.should(have.text(text_to_match))
