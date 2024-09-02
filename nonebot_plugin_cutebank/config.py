from typing import Set
from pathlib import Path

from nonebot import get_plugin_config
from pydantic import BaseModel


class ConfigModel(BaseModel):
    nickname: Set[str]

    cutebank_path: Path = Path(__file__).parent / "data.json"

    pass


config: ConfigModel = get_plugin_config(ConfigModel)
