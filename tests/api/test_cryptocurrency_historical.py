import pytest
from requests import codes

from demo_autoqa_coinmarketcap.api.models.error_response import ErrorResponse
from demo_autoqa_coinmarketcap.utils.validators import is_object_matches_model


@pytest.mark.parametrize('endpoint_historical', [
    '/v1/cryptocurrency/listings/historical',
    '/v2/cryptocurrency/quotes/historical',
    '/v2/cryptocurrency/ohlcv/historical'
])
def test_if_historical_data_unavailable_by_default(cmc_api, endpoint_historical):
    status_code, response = cmc_api.get(endpoint_historical)
    assert status_code == codes.FORBIDDEN
    assert response['status']['error_message'] == "Your API Key subscription plan doesn't support this endpoint."
    assert response['status']['error_code'] == 1006
    assert is_object_matches_model(response, ErrorResponse)