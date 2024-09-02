<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-cutebank

_✨ NoneBot 插件简单描述 ✨_

<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>

## 📖 介绍

基于NoneBot2的一个自用插件，根据词库回复@bot的消息以及对bot的戳一戳消息。\
词库主要为可爱风，从网上随便找的

## 💿 安装

手动将文件夹丢到src/plugins文件夹内（不会在pypi发布）

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

|         配置项         | 必填 |    默认值    |   说明    |
|:-------------------:|:--:|:---------:|:-------:|
|      NICKNAME       | 否  |    bot    |  bot昵称  |
|    CUTEBANK_PATH    | 否  | data.json |  词库路径   |
| CUTEBANK_SIMILARITY | 否  |    70     | 匹配精确度阈值 |

## 🎉 使用
### 指令表
|      指令       | 权限 | 需要@ | 范围 |  说明  |
|:-------------:|:--:|:---:|:--:|:----:|
|    戳一戳bot     | 群员 |  否  | 群聊 | 触发回复 |
| @bot+想对bot说的话 | 群员 |  是  | 群聊 | 触发回复 |

## 💡 鸣谢
### [nonebot-plugin-picstatus](https://github.com/lgc-NB2Dev/nonebot-plugin-picstatus)
-模糊搜索代码参考
### [nonebot_plugin_smart_reply](https://github.com/Special-Week/nonebot_plugin_smart_reply/)
-响应逻辑代码参考

