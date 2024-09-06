from nonebot.plugin import PluginMetadata
from nonebot.plugin.on import on_message, on_notice
from nonebot.rule import to_me, is_type

from .config import ConfigModel
from .keywordhandle import key_word_module, GroupMessageEvent


__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="自用轻量化词库",
    description="根据词库回复信息",
    usage="@我+[想对我说的话]\n或戳一戳我",
    type="application",
    homepage="https://github.com/WuSheng125/nonebot-plugin-cutebank",
    config=ConfigModel,
    extra={"License": "MIT", "Author": "WuSheng125"},
)

# 戳一戳响应器 优先级1, 不会向下阻断, 条件: 戳一戳bot触发
on_notice(rule=to_me(), block=False, handlers=[key_word_module.poke_handle])

# 普通回复响应器, 优先级999, 条件: 艾特bot就触发
on_message(
    rule=to_me() and is_type(GroupMessageEvent), priority=999, block=False, handlers=[key_word_module.regular_reply]
)
