import allure
import pytest
from allure_commons.types import Severity
from requests import codes

from demo_autoqa_coinmarketcap.api.models.error_response import ErrorResponse
from demo_autoqa_coinmarketcap.utils.validators import is_object_matches_model


@pytest.mark.api
@pytest.mark.regress
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'master_klinka')
@allure.story("API Access Restrictions")
@allure.title("Verify Unavailability of Historical Data by Default")
@allure.description(
    'This test verifies that access to historical cryptocurrency data endpoints is restricted by default. '
    'It checks for a `FORBIDDEN` response status when accessing various historical data endpoints without '
    'the necessary subscription plan.')
@pytest.mark.parametrize('endpoint_historical', [
    '/v1/cryptocurrency/listings/historical',
    '/v2/cryptocurrency/quotes/historical',
    '/v2/cryptocurrency/ohlcv/historical'
])
def test_if_historical_data_unavailable_by_default(cmc_api, endpoint_historical):
    with allure.step('Send GET Request to Each Historical Data Endpoint'):
        status_code, response = cmc_api.get(endpoint_historical)

    with allure.step(f'Verify Response Status Code is {codes.FORBIDDEN}'):
        assert status_code == codes.FORBIDDEN

    with allure.step('Check API Error Message and Code for Subscription Plan Restrictions'):
        assert response['status']['error_message'] == "Your API Key subscription plan doesn't support this endpoint."
        assert response['status']['error_code'] == 1006

    with allure.step('Validate Response Matches ErrorResponse Model'):
        assert is_object_matches_model(response, ErrorResponse)
