from datetime import datetime
from typing import Optional, List, Dict, Union

from pydantic import BaseModel, HttpUrl

from demo_autoqa_coinmarketcap.api.models.status import Status


class Urls(BaseModel):
    website: List[HttpUrl]
    twitter: List[HttpUrl]
    message_board: List[HttpUrl]
    chat: List[HttpUrl]
    facebook: List[HttpUrl]
    explorer: List[HttpUrl]
    reddit: List[HttpUrl]
    technical_doc: List[HttpUrl]
    source_code: List[HttpUrl]
    announcement: List[HttpUrl]


class ContractAddress(BaseModel):
    contract_address: str
    platform: Optional[dict]

class InfoData(BaseModel):
    id: int
    name: str
    symbol: str
    category: str
    description: str
    slug: str
    logo: HttpUrl
    subreddit: str
    notice: Optional[str] = None
    tags: List[str]
    # tag_names: Optional[List[str]]
    # tag_groups: Optional[List[str]]
    urls: Urls
    platform: Optional[str] = None
    date_added: datetime
    twitter_username: str
    is_hidden: int
    date_launched: Optional[datetime]
    contract_address: Optional[List[ContractAddress]]  # Use the new ContractAddress model
    self_reported_circulating_supply: Optional[int] = None
    self_reported_tags: Optional[List[str]] = None
    self_reported_market_cap: Optional[int] = None
    infinite_supply: bool

class InfoResponse(BaseModel):
    status: Status
    data: Dict[str, Union[List[InfoData]]]