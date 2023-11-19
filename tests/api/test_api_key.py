from requests import codes

from demo_autoqa_coinmarketcap.api.models.error_response import ErrorResponse
from demo_autoqa_coinmarketcap.utils.validators import is_object_matches_model
from tests.conftest import not_valid_api_key, empty_api_key


@not_valid_api_key
def test_error_if_api_key_not_valid(cmc_api):
    status_code, response = cmc_api.get('/v2/cryptocurrency/info?symbol=BTC')

    assert status_code == codes.UNAUTHORIZED

    assert is_object_matches_model(response, ErrorResponse)

    assert response['status']['error_message'] == "This API Key is invalid."
    assert response['status']['error_code'] == 1001


@empty_api_key
def test_error_if_api_key_is_empty(cmc_api):
    status_code, response = cmc_api.get('/v2/cryptocurrency/info?symbol=BTC')

    assert status_code == codes.UNAUTHORIZED

    assert is_object_matches_model(response, ErrorResponse)

    assert response['status']['error_message'] == "API key missing."
    assert response['status']['error_code'] == 1002

