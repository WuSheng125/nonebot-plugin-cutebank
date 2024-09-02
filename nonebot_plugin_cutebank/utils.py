import random
import json
from pathlib import Path
from typing import Tuple, Union, Dict
from fuzzywuzzy import process

from .config import config


class Utils:
    def __init__(self) -> None:
        """初始化"""
        self.bot_nickname: str = next(iter(config.nickname), 'bot')
        self.poke_reply: Tuple = (
            f"别戳了，{self.bot_nickname}怕疼QwQ",
            f"呜呜，再戳{self.bot_nickname}脸都要肿了",
            f"戳坏了{self.bot_nickname}，你赔得起吗？",
            f"再戳{self.bot_nickname}，我要叫我主人了",
            f"别老戳{self.bot_nickname}了，您歇会吧~",
            f"再戳{self.bot_nickname}，咬你了嗷~",
            "想好了再戳，(*-`ω´-)✄",
            "喂，110吗，有人老戳我",
            "嗷呜嗷呜...恶龙咆哮┗|｀O′|┛",
            "再戳我让你变成女人，嘿嘿",
            "不要戳我了 >_<",
            "不要这样子啦(*/ω＼*)",
            "不要再戳了(害怕ing)",
            "还戳，哼(つд⊂)（生气）",
            "再戳，小心我顺着网线找你.",
            "咱要型气了o(>﹏<)o",
            "嘿嘿，好舒服呀(bushi)",
            "乖~好了好了，别戳了~",
            "啊呜，你有什么事吗？",
            "你再戳！",
            "别戳了别戳了再戳就坏了555",
            "我爪巴爪巴，球球别再戳了",
            f"请不要戳{self.bot_nickname} >_<",
            "放手啦，不给戳QAQ",
            f"喂(#`O′) 戳{self.bot_nickname}干嘛！",
            "戳坏了，赔钱！",
            "戳坏了",
            "嗯……不可以……啦……不要乱戳",
            "那...那里...那里不能戳...绝对...",
            "(。´・ω・)ん?",
            "正在关闭对您的所有服务...关闭成功",
            "啊呜，太舒服刚刚竟然睡着了。什么事？",
            "正在定位您的真实地址...定位成功。轰炸机已起飞",
        )
        self.hello_reply: Tuple = (
            "你好！",
            "哦豁？！",
            "你好！Ov<",
            f"库库库，呼唤{self.bot_nickname}做什么呢",
            "我在呢！",
            f"呼呼，叫{self.bot_nickname}干嘛",
        )
        self.nonsense: Tuple = (
            "你好啊",
            "你好",
            "在吗",
            "在不在",
            "您好",
            "您好啊",
            "你好",
            "在",
        )
        self.keyword_path: Path = config.cutebank_path
        self.anime_thesaurus: Dict = json.load(
            open(self.keyword_path, "r", encoding="utf-8")
        )

    async def rand_hello(self) -> str:
        """随机问候语"""
        return random.choice(self.hello_reply)

    async def rand_poke(self) -> str:
        """随机戳一戳"""
        return random.choice(self.poke_reply)

    async def get_chat_result(self, text: str, username: str) -> Union[str, None]:
        """从字典中返回结果"""
        keys = self.anime_thesaurus.keys()
        res = process.extractOne(text, keys)
        if res[1] > 70:
            msg = random.choice(self.anime_thesaurus[res[0]]).format(username=username, bot_nickname=self.bot_nickname)
        else:
            msg = f'{self.bot_nickname}听不懂哦~'

        return msg


utils = Utils()
