from demo_autoqa_coinmarketcap.api.base_request import BaseRequest


class CoinmarketcapAPI(BaseRequest):
    def __init__(self):
        super().__init__()

    def get(self, endpoint, params=None):
        status_code, data = self.request('GET', endpoint, params=params)
        return status_code, data


cmc_api = CoinmarketcapAPI()
