import json
import time
from urllib.parse import urljoin

import allure
import requests
import structlog
from allure import step
from allure_commons.types import AttachmentType
from curlify import to_curl

from config import config


class BaseRequest:
    def __init__(self):
        self.api_url = config.api_url
        self.api_key = config.api_key
        self.session = requests.Session()
        self.session.headers.update(
            {"X-CMC_PRO_API_KEY": self.api_key, "Accept": "application/json"}
        )
        self.log = structlog.get_logger()
        self.request_delay = config.api_request_delay

    @allure.step("{method}: {endpoint}")
    def request(self, method, endpoint, **kwargs):
        url = urljoin(self.api_url, endpoint)
        self.log.msg(
            "request",
            method=method,
            base_url=self.api_url,
            endpoint=endpoint,
            kwargs=kwargs if kwargs else None,
        )
        time.sleep(self.request_delay)
        response = self.session.request(method, url, **kwargs)
        allure.attach(
            body=to_curl(response.request),
            name="cURL",
            attachment_type=AttachmentType.TEXT,
            extension="txt",
        )
        self.log.msg(
            "response",
            method=method,
            base_url=self.api_url,
            endpoint=endpoint,
            status_code=response.status_code,
            response_text=response.text,
        )
        try:
            response_data = response.json()
            allure.attach(
                body=json.dumps(response_data, indent=4, ensure_ascii=False),
                name="response body",
                attachment_type=AttachmentType.JSON,
                extension="json",
            )
        except Exception as e:
            self.log.msg(e)
            response_data = None

        return response.status_code, response_data
