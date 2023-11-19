from selene import browser, have, be, query


class CurrencyPage:
    def __init__(self):
        self.converter_content = browser.element('.converter-content')
        pass

    def open_default(self):
        browser.open('/currencies/bitcoin/')

    def open_by_name(self, currency_name):
        browser.open(f'/currencies/{currency_name}/')

    def should_be_equeal_to_page_coin_name(self, text_to_match):
        page_coin_name = browser.element('.coin-name-pc').get(query.text)
        assert text_to_match == page_coin_name

    def should_be_equal_to_page_coin_symbol(self, text_to_match):
        page_coin_symbol = browser.element('span[data-role="coin-symbol"]').get(query.text)
        assert text_to_match == page_coin_symbol

    def should_have_price(self, input_price: float):
        input_price_rounded = round(input_price, 2)
        page_price = self.converter_content.all('input')[-1].get(query.attribute('value'))
        page_price_rounded = round(float(page_price), 2)
        # prices always not the same
        assert input_price_rounded == page_price_rounded
