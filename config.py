import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
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
    browser_timeout: int = 15
    default_browser_name: str = 'chrome'
    default_browser_version: str = '100.0'
    test_user: TestUser = TestUser()
    selenoid_user: SelenoidUser = SelenoidUser()
    cmc_user: CoinMarketCupUser = CoinMarketCupUser()
    mobile_context: str = 'local_real'


config = Config()

if config.mobile_context == 'bstack':
    load_dotenv()
    load_dotenv(os.path.join(BASE_DIR, '.env.bstack'))
elif config.mobile_context == 'local_real':
    load_dotenv(os.path.join(BASE_DIR, '.env.local_real'))
else:
    load_dotenv(os.path.join(BASE_DIR, '.env.local_emulator'))

remote_url = os.getenv('REMOTE_URL')
udid = os.getenv('UDID')
device_name = os.getenv('DEVICE_NAME')

apk_path = os.getenv('APP_ID') if config.mobile_context == 'bstack' \
    else os.path.join(BASE_DIR, 'apk', os.getenv('APP_ID'))


def driver_options():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'app': apk_path,
        'appWaitActivity': 'com.coinmarketcap.*',

    })

    if device_name:
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))

    if config.mobile_context == 'bstack':
        options.set_capability('platformVersion', '9.0')
        options.set_capability(
            "bstack:options", {
                "userName": os.getenv('BSTACK_USER'),
                "accessKey": os.getenv('BSTACK_ACCESS_KEY'),
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test"
            },
        )

    return options
