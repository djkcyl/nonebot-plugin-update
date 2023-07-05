from nonebot import get_driver
from pydantic import BaseModel


class Config(BaseModel):
    npu_auto_check: bool = True
    npu_check_prerelease: bool = False


plugin_config = Config.parse_obj(get_driver().config)
