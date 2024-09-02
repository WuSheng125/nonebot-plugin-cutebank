# import random
from typing import Union

from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import (
    # Message,
    MessageEvent,
    MessageSegment,
    PokeNotifyEvent,
    PrivateMessageEvent,
)

from .utils import utils


class KeyWordModule:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def poke_handle(matcher: Matcher, event: PokeNotifyEvent) -> None:
        """戳一戳回复, 私聊会报错, 暂时摸不着头脑"""
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
