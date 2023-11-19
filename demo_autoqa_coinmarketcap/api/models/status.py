from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Status(BaseModel):
    timestamp: datetime
    error_code: int
    error_message: Optional[str]
    elapsed: int
    credit_count: int
    notice: Optional[str] = None
