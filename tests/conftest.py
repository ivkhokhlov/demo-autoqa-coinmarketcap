import pytest

from demo_autoqa_coinmarketcap.api.cmc_api import CoinmarketcapAPI


@pytest.fixture()
def cmc_api(request):
    param = getattr(request, 'param', 'valid_api_key')

    cmc_api = CoinmarketcapAPI()

    if param == 'not_valid_api_key':
        cmc_api.session.headers["X-CMC_PRO_API_KEY"] = '1234567890'
    elif param == 'empty_api_key':
        cmc_api.session.headers.pop('X-CMC_PRO_API_KEY', None)
    elif param == 'valid_api_key':
        pass
    else:
        pass

    return cmc_api


valid_api_key = pytest.mark.parametrize('cmc_api', ['valid_api_key'], indirect=True)
not_valid_api_key = pytest.mark.parametrize('cmc_api', ['not_valid_api_key'], indirect=True)
empty_api_key = pytest.mark.parametrize('cmc_api', ['empty_api_key'], indirect=True)
