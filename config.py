from pydantic_settings import BaseSettings, SettingsConfigDict
from uuid import UUID


class TestUser(BaseSettings):
    email: str = ""
    password: str = ""


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    api_url: str = 'https://pro-api.coinmarketcap.com/'
    api_key: UUID
    test_user: TestUser = TestUser()


base_settings = Config()