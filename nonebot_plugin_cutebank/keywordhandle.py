# import random
from typing import Union, Dict, Any

from nonebot import require
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import (
    # Message,
    MessageEvent,
    MessageSegment,
    PokeNotifyEvent,
    PrivateMessageEvent,
)

from .utils import utils
from .config import config

limit_all = require("nonebot_plugin_apscheduler").scheduler
limit_all_data: Dict[str, Any] = {}
limit_num = config.cutebank_limit


@limit_all.scheduled_job('interval', hours=0, minutes=1)
def limit_all():
    # 重置消息字典
    global limit_all_data
    limit_all_data = {}
    # logger.success("已重置消息字典！")


def limit_all_run(user_id: str):
    global limit_all_data
    user_id = str(user_id)
    num = None
    tip = None
    if limit_num == 0:
        return None
    if user_id in limit_all_data.keys():
        num = limit_all_data[user_id]["num"]
        tip = limit_all_data[user_id]["tip"]
    else:
        limit_all_data[user_id] = {"num": 0, "tip": False}
        num = 0
        tip = False
    num += 1
    if num > limit_num and tip is False:
        tip = True
        limit_all_data[user_id]["num"] = num
        limit_all_data[user_id]["tip"] = tip
        return True
    if num > limit_num and tip is True:
        limit_all_data[user_id]["num"] = num
        return False
    else:
        limit_all_data[user_id]["num"] = num
        return None


class KeyWordModule:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def poke_handle(matcher: Matcher, event: PokeNotifyEvent) -> None:
        """戳一戳回复, 私聊会报错, 暂时摸不着头脑"""
        # 私聊信息直接结束处理
        if isinstance(event, PrivateMessageEvent):
            return
        # 回复频率限制
        limit_type = limit_all_run(str(event.group_id))
        if limit_type is True:
            await matcher.finish(MessageSegment.text('不理你们了，哼！'))
        elif limit_type is False:
            await matcher.finish()

        if event.is_tome():
            '''有报错，看不懂api喵
            probability: float = random.random()
            if probability < 0.33 and event.group_id is not None:
                # 33% 概率戳回去
                await matcher.send(Message(MessageSegment("poke", {"qq": event.user_id})))
            else:'''
            await matcher.send(await utils.rand_poke())

    @staticmethod
    async def regular_reply(matcher: Matcher, event: MessageEvent) -> None:
        """普通回复"""
        # 私聊信息直接结束处理
        if isinstance(event, PrivateMessageEvent):
            return
        # 回复频率限制
        limit_type = limit_all_run(str(event.group_id))
        if limit_type is True:
            await matcher.finish(MessageSegment.text('不理你们了，哼！'))
        elif limit_type is False:
            await matcher.finish()
        # 获取消息文本
        msg = event.get_message().extract_plain_text()
        # 如果是光艾特bot(没消息返回)或者打招呼的话,就回复以下内容
        if (not msg) or msg.isspace() or msg in utils.nonsense:
            await matcher.finish(MessageSegment.text(await utils.rand_hello()))
        # 获取用户nickname
        nickname: Union[str, None] = event.sender.card or event.sender.nickname
        # 从字典里获取结果
        result: Union[str, None] = await utils.get_chat_result(msg, nickname)

        await matcher.finish(MessageSegment.text(result), reply_message=True)


key_word_module = KeyWordModule()
