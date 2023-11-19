import allure
import pytest
from allure_commons.types import Severity

from demo_autoqa_coinmarketcap.pages.manager import cmc_ui


@pytest.mark.ui
@pytest.mark.regress
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Search Functionality")
@allure.title("Search Functionality for Cryptocurrency Symbols")
@allure.description(
    "Tests the search functionality on the main page for various cryptocurrency symbols like BTC, LTC, and ETH. "
    "It covers opening the main page, using the search feature, selecting a result from the suggestions, and verifying "
    "that the resulting currency page matches the expected coin name and symbol."
)
@pytest.mark.parametrize('symbol,name', [('BTC', 'Bitcoin'),
                                         ('LTC', 'Litecoin'),
                                         ('ETH', 'Ethereum'),
                                         ])
def test_search(symbol, name):
    with allure.step("Open Main Page"):
        cmc_ui.main_page.open()

    with allure.step("Initiate Search Process"):
        cmc_ui.main_page.click_search()

    with allure.step(f"Enter Symbol in Search and Verify Suggestions: {symbol}"):
        cmc_ui.main_page.type_desktop_input_search(symbol)
        cmc_ui.main_page.should_tippy_content_have_text(symbol)

    with allure.step("Select From Search Suggestions"):
        cmc_ui.main_page.click_first_tippy_result()

    with allure.step("Verify Correct Currency Page Opens"):
        cmc_ui.currency_page.should_be_equeal_to_page_coin_name(name)
        cmc_ui.currency_page.should_be_equal_to_page_coin_symbol(symbol)


@pytest.mark.ui
@pytest.mark.regress
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Main Page Functionality")
@allure.title("Verify Tab Names on Main Page")
@allure.description(
    "Tests the presence of specific tab names on the main page. It verifies that tabs such as 'Cryptocurrencies', "
    "'Categories', and others are correctly displayed."
)
def test_table_buttons_names():
    tab_names = [
        'Cryptocurrencies',
        'Categories',
        'Bitcoin Ecosystem',
        'FTX Bankruptcy Estate',
        'Telegram Bot',
        'Real World Assets'
    ]

    with allure.step("Open Main Page"):
        cmc_ui.main_page.open()

    with allure.step("Verify Presence of Tab Names"):
        cmc_ui.main_page.should_tabs_be_on_page(tab_names)


@pytest.mark.ui
@pytest.mark.regress
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Currency Navigation")
@allure.title("Verify Navigation to Currency Page from Main Page")
@allure.description(
    "Tests the functionality of navigating to a specific cryptocurrency's page from the main page by clicking on "
    "the cryptocurrency row. The test ensures that selecting a cryptocurrency symbol like BTC, LTC, or ETH leads "
    "to the correct currency page, verifying both the coin name and symbol."
)
@pytest.mark.parametrize('symbol, name', [('ETH', 'Ethereum')])
def test_click_on_currency_from_main_page(symbol, name):
    with allure.step("Open Main Page"):
        cmc_ui.main_page.open()

    with allure.step(f"Click on Cryptocurrency Row for Symbol: {symbol}"):
        cmc_ui.main_page.click_on_row_by_symbol(symbol)

    with allure.step("Verify Currency Page Details"):
        cmc_ui.currency_page.should_be_equeal_to_page_coin_name(name)
        cmc_ui.currency_page.should_be_equal_to_page_coin_symbol(symbol)
