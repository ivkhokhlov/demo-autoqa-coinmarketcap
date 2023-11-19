from pydantic import BaseModel

from demo_autoqa_coinmarketcap.api.models.status import Status


class ErrorResponse(BaseModel):
    status: Status
