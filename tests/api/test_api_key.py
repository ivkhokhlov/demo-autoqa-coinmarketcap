import allure
import pytest
from allure_commons.types import Severity
from requests import codes

from demo_autoqa_coinmarketcap.api.models.error_response import ErrorResponse
from demo_autoqa_coinmarketcap.utils.validators import is_object_matches_model
from tests.conftest import not_valid_api_key, empty_api_key


@pytest.mark.api
@pytest.mark.smoke
@allure.label('owner', 'master_klinka')
@allure.severity(Severity.BLOCKER)
@allure.story("API key integration")
@allure.title("Verify Error Response When API Key is Invalid")
@allure.description("Tests the API's response when an invalid API key is used to request cryptocurrency information.")
@not_valid_api_key
def test_error_if_api_key_not_valid(cmc_api):
    with allure.step('Send GET request with not valid API key'):
        status_code, response = cmc_api.get('/v2/cryptocurrency/info?symbol=BTC')

    with allure.step(f'Verify response status code is {codes.UNAUTHORIZED}'):
        assert status_code == codes.UNAUTHORIZED

    with allure.step('Validate response matches the ErrorResponse model'):
        assert is_object_matches_model(response, ErrorResponse)

    with allure.step('Check error message and code for invalid API key'):
        assert response['status']['error_message'] == "This API Key is invalid."
        assert response['status']['error_code'] == 1001


@pytest.mark.api
@pytest.mark.smoke
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'master_klinka')
@allure.story("API key integration")
@allure.title("Check API Response with Empty API Key")
@allure.description(
    'Ensures the API returns an error when an empty API key is provided for cryptocurrency information requests.')
@empty_api_key
def test_error_if_api_key_is_empty(cmc_api):
    with allure.step('Send GET request with an empty API key'):
        status_code, response = cmc_api.get('/v2/cryptocurrency/info?symbol=BTC')

    with allure.step('Verify response status code is UNAUTHORIZED'):
        assert status_code == codes.UNAUTHORIZED

    with allure.step('Validate response matches the ErrorResponse model'):
        assert is_object_matches_model(response, ErrorResponse)

    with allure.step('Check error message and code for missing API key'):
        assert response['status']['error_message'] == "API key missing."
        assert response['status']['error_code'] == 1002
