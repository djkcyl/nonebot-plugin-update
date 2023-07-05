from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata, require

from .check import check_update
from .version import __version__

require("nonebot_plugin_apscheduler")
require("nonebot_plugin_localstore")


__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-update",
    description="用于检测 Nonebot 插件更新的 Nonebot 插件",
    usage="发送 /npu help 查看帮助",
    homepage="https://github.com/Aunly/nonebot-plugin-update",
    type="application",
    supported_adapters={"~onebot.v11"},
    extra={
        "author": "djkcyl",
        "version": __version__,
    },
)


manual_check = on_command("npu check", permission=SUPERUSER)


@manual_check.handle()
async def main():
    plugin_update = await check_update(False, True)
    if not plugin_update.plugins:
        await manual_check.finish("没有可用更新")
    msg = "以下插件有可用更新：\n"
    for plugin in plugin_update.plugins:
        msg += f"{plugin.name}：{plugin.local_version} -> {plugin.remote_version}\n"
    await manual_check.finish(msg)
