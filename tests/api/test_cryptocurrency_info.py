import allure
import pytest
from allure_commons.types import Severity
from requests import codes

from demo_autoqa_coinmarketcap.api.models.error_response import ErrorResponse
from demo_autoqa_coinmarketcap.api.models.info import InfoResponse
from demo_autoqa_coinmarketcap.utils.validators import is_object_matches_model


@pytest.mark.api
@pytest.mark.regress
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'master_klinka')
@allure.story("Currency Data Retrieval")
@allure.title("Verify Retrieval of Currency Information by Symbol")
@allure.description(
    'This test verifies that the API correctly retrieves information for specified cryptocurrency symbols. '
    'It checks for a `OK` response status when querying the cryptocurrency info endpoint with different symbols '
    'and validates that the response contains the requested symbols.'
)
@pytest.mark.parametrize('symbol', ['BTC', 'BTC,ETH', 'EUR,RUB,USD'])
def test_get_currency_by_symbol(cmc_api, symbol):
    with allure.step(f'Send GET Request for Symbol(s) {symbol}'):
        status_code, response = cmc_api.get(f'/v2/cryptocurrency/info?symbol={symbol}')

    with allure.step(f'Verify Response Status Code is {codes.OK}'):
        assert status_code == codes.OK

    with allure.step('Validate Response Matches InfoResponse Model'):
        assert is_object_matches_model(response, InfoResponse)

    with allure.step('Check Response Contains Requested Symbols'):
        assert symbol.split(',') == list(response.get('data').keys())


@pytest.mark.api
@pytest.mark.regress
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Symbol Validation in API")
@allure.title("Verify Error Response for Non-Existent Currency Symbols")
@allure.description("Tests the API's response when non-existent currency symbols are used in requests. "
                    "It verifies that a BAD_REQUEST response is returned with specific error messages "
                    "indicating invalid symbol values.")
@pytest.mark.parametrize('symbol', ['NONEXISTED', 'BTC,NONEXISTED', 'NONEXISTED,BTC', 'NONEXISTED,NONEXISTED'])
def test_error_if_symbol_not_exists(cmc_api, symbol):
    with allure.step(f'Send GET Request with Non-Existent Symbol {symbol}'):
        status_code, response = cmc_api.get(f'/v2/cryptocurrency/info?symbol={symbol}')

    with allure.step('Validate Response Matches ErrorResponse Model'):
        assert is_object_matches_model(response, ErrorResponse)

    with allure.step(f'Verify Response Status Code is {codes.BAD_REQUEST}'):
        assert status_code == codes.BAD_REQUEST
        assert response['status']['error_code'] == codes.BAD_REQUEST

    with allure.step('Check Error Message for Invalid Symbol'):
        assert 'Invalid value for "symbol":' in response['status']['error_message']
        assert 'NONEXISTED' in response['status']['error_message']


@pytest.mark.api
@pytest.mark.regress
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Symbol Validation in API")
@allure.title("Verify Error Response for Empty Currency Symbol")
@allure.description(
    "Tests the API's response when an empty currency symbol is used in a request. "
    "It verifies that a `BAD_REQUEST` response is returned, indicating the symbol parameter cannot be empty.")
def test_error_if_symbol_is_empty(cmc_api):
    with allure.step('Send GET Request with Empty Symbol'):
        status_code, response = cmc_api.get("/v2/cryptocurrency/info?symbol=''")

    with allure.step('Verify Response Status Code is BAD_REQUEST'):
        assert status_code == codes.BAD_REQUEST

    with allure.step('Validate Response Matches ErrorResponse Model'):
        assert is_object_matches_model(response, ErrorResponse)


@pytest.mark.api
@pytest.mark.regress
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'master_klinka')
@allure.story("Symbol Validation in API")
@allure.title("Verify Error Response for Invalid Currency Symbols")
@allure.description(
    "Tests the API's response for various invalid currency symbols. "
    "It checks that a `BAD_REQUEST` response is returned with a specific error message indicating "
    "the symbol parameter should only include valid alphanumeric cryptocurrency symbols.")
@pytest.mark.parametrize('symbol', ['{}', '___', '!'])
def test_error_if_symbol_not_valid(cmc_api, symbol):
    with allure.step(f'Send GET Request with Invalid Symbol {symbol}'):
        status_code, response = cmc_api.get(f'/v2/cryptocurrency/info?symbol={symbol}')

    with allure.step('Validate Response Matches ErrorResponse Model'):
        assert is_object_matches_model(response, ErrorResponse)

    with allure.step(f'Verify Response Status Code is {codes.BAD_REQUEST} and Check Error Message'):
        assert status_code == codes.BAD_REQUEST
        assert response['status']['error_code'] == codes.BAD_REQUEST
        assert response['status'][
                   'error_message'] == '"symbol" should only include comma-separated alphanumeric cryptocurrency symbols'
