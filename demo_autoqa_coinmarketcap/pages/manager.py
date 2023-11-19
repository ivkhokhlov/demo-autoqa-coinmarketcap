from demo_autoqa_coinmarketcap.pages.main import MainPage
from demo_autoqa_coinmarketcap.pages.login import LoginPage
from demo_autoqa_coinmarketcap.pages.currency import CurrencyPage


class ApplicationManager():
    def __init__(self):
        self.main_page = MainPage()
        self.login_page = LoginPage()
        self.currency_page = CurrencyPage()


cmc_ui = ApplicationManager()