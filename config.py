import os

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.dirname(__file__)


class TestUser(BaseSettings):
    email: str = ""
    password: str = ""


class SelenoidUser(BaseSettings):
    login: str = ""
    password: str = ""

class CoinMarketCupUser(BaseSettings):
    login: str = ""
    password: str = ""


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, '.env'),
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    api_url: str = 'https://pro-api.coinmarketcap.com/'
    api_key: str
    api_request_delay: int = 2
    browser_timeout: int = 10
    test_user: TestUser = TestUser()
    selenoid_user: SelenoidUser = SelenoidUser()
    cmc_user: CoinMarketCupUser = CoinMarketCupUser()


config = Config()
print(config)
