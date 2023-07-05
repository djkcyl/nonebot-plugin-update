from enum import Enum, auto
from pydantic import BaseModel
from typing import List, Optional


class SkipType(Enum):
    CURRENT = auto()
    FOREVER = auto()


class BlackItem(BaseModel):
    name: str
    version: str
    skip_type: SkipType


class Blacklist(BaseModel):
    plugins: List[BlackItem] = []


class PluginInfo(BaseModel):
    name: str
    local_version: str
    remote_version: Optional[str]
    pre_release: bool


class CheckResult(BaseModel):
    plugins: List[PluginInfo] = []
