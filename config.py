from pydantic import UUID4

from pydantic_settings import BaseSettings, SettingsConfigDict
import os

BASE_DIR = os.path.dirname(__file__)


class TestUser(BaseSettings):
    email: str = ""
    password: str = ""


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, '.env'),
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    api_url: str = 'https://pro-api.coinmarketcap.com/'
    api_key: str
    test_user: TestUser = TestUser()


config = Config()
