import pytest
from requests import codes

from demo_autoqa_coinmarketcap.api.models.error_response import ErrorResponse
from demo_autoqa_coinmarketcap.api.models.info import InfoResponse
from demo_autoqa_coinmarketcap.utils.validators import is_object_matches_model


@pytest.mark.parametrize('symbol', ['BTC', 'BTC,ETH', 'EUR,RUB,USD'])
def test_get_currency_by_symbol(cmc_api, symbol):
    status_code, response = cmc_api.get(f'/v2/cryptocurrency/info?symbol={symbol}')

    assert status_code == codes.OK
    assert symbol.split(',') == list(response.get('data').keys())
    assert is_object_matches_model(response, InfoResponse)


@pytest.mark.parametrize('symbol', ['NONEXISTED', 'BTC,NONEXISTED', 'NONEXISTED,BTC', 'NONEXISTED,NONEXISTED'])
def test_error_if_symbol_not_exists(cmc_api, symbol):
    status_code, response = cmc_api.get(f'/v2/cryptocurrency/info?symbol={symbol}')

    # проверка статус кода
    assert status_code == codes.BAD_REQUEST
    assert response['status']['error_code'] == codes.BAD_REQUEST
    assert 'Invalid value for "symbol":' in response['status']['error_message']
    assert 'NONEXISTED' in response['status']['error_message']

    # валидация схемы
    assert is_object_matches_model(response, ErrorResponse)


def test_error_if_symbol_is_empty(cmc_api):
    status_code, response = cmc_api.get("/v2/cryptocurrency/info?symbol=''")

    assert status_code == codes.BAD_REQUEST
    assert is_object_matches_model(response, ErrorResponse)


@pytest.mark.parametrize('symbol', ['{}', '___', '!'])
def test_error_if_symbol_not_valid(cmc_api, symbol):
    status_code, response = cmc_api.get(f'/v2/cryptocurrency/info?symbol={symbol}')

    # проверка статус кода
    assert status_code == codes.BAD_REQUEST
    assert response['status']['error_code'] == codes.BAD_REQUEST
    assert response['status']['error_message'] == '"symbol" should only include comma-separated alphanumeric cryptocurrency symbols'

    # валидация схемы
    assert is_object_matches_model(response, ErrorResponse)
