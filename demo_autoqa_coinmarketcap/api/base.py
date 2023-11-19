import json

import allure
import structlog
from allure import step
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import Session


class BaseRequest:
    def __init__(self):
        self.base_url = BASE_URL
        self.log = structlog.get_logger()
        self.session = session if session else Session()

    @step("Отправить запрос: {method}, {endpoint}")
    def request(self, method, endpoint, **kwargs):

        self.log.msg(
            "request",
            method=method,
            base_url=self.base_url,
            endpoint=endpoint,
            kwargs=kwargs if kwargs else None,
        )

        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, verify=False, **kwargs)

        allure.attach(
            body=to_curl(response.request),
            name="cURL",
            attachment_type=AttachmentType.TEXT,
            extension="txt",
        )

        self.log.msg(
            "response",
            method=method,
            base_url=self.base_url,
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
