import allure
import pytest
from allure_commons.types import Severity

from demo_autoqa_coinmarketcap.pages.manager import cmc_ui


@pytest.mark.ui
@pytest.mark.api
@pytest.mark.regress
@allure.severity(Severity.TRIVIAL)
@allure.story("Curency Page")
@allure.label('owner', 'master_klinka')
@allure.title("Verify Currency Price Consistency Between API and UI")
@allure.description(
    "Compares the currency price data from the API against the price displayed on the UI for consistency. "
    "This test checks if the price for a specified currency (e.g., Bitcoin) is the same when retrieved via the API "
    "and seen on the UI. Expected to fail due to price fluctuation."
)
@pytest.mark.xfail(reason='Prices always not the same, expeted failing')
@pytest.mark.parametrize('symbol,name', [('BTC', 'bitcoin')])
def test_currency_price_consistency_api_vs_page(cmc_api, symbol, name):
    with allure.step(f"Open Currency Page by Name: {name}"):
        cmc_ui.currency_page.open_by_name(name)

    with allure.step(f"Retrieve Currency Price via API for Symbol: {symbol}"):
        _, response = cmc_api.get(f'/v2/cryptocurrency/quotes/latest?symbol={symbol}')
        price_via_api = response['data']['BTC'][0]['quote']['USD']['price']

    with allure.step("Verify Price Consistency Between API and UI"):
        cmc_ui.currency_page.should_have_price(price_via_api)
