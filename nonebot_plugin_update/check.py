import httpx
import contextlib

from importlib import metadata
from packaging.version import parse

from nonebot import logger
from nonebot.plugin import get_loaded_plugins
from nonebot_plugin_localstore import get_data_file


from .model import Blacklist, CheckResult, PluginInfo, SkipType

BLACK_LIST_FILE = get_data_file("nonebot_plugin_update", "black_list.json")
if not BLACK_LIST_FILE.exists():
    BLACK_LIST = Blacklist(plugins=[])
    BLACK_LIST_FILE.write_text(BLACK_LIST.json())
else:
    BLACK_LIST = Blacklist.parse_file(BLACK_LIST_FILE)


async def get_remote_version(plugin_name: str):
    with contextlib.suppress(Exception):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"https://pypi.org/pypi/{plugin_name}/json")
            resp = resp.json()
            return sorted(resp["releases"].keys(), key=parse)


async def check_update(skip_blacklist: bool, pre_release: bool):
    plugins = get_loaded_plugins()
    logger.info(f"[NPU] 正在检查更新，共有 {len(plugins)} 个插件")
    result = CheckResult(plugins=[])
    for plugin in plugins:
        if skip_blacklist or plugin.name in [
            i.name for i in BLACK_LIST.plugins if i.skip_type == SkipType.FOREVER
        ]:
            logger.info(f"[NPU] 跳过插件 {plugin.name} 的更新检查")
        local_version = parse(metadata.version(plugin.module_name))
        remote_version_list = await get_remote_version(plugin.name)
        if not remote_version_list:
            logger.info(f"[NPU] 插件 {plugin.name} 无法获取远程版本")
            continue

        if pre_release:
            remote_version_list = [i for i in remote_version_list if parse(i).is_prerelease]
            if not remote_version_list:
                logger.info(f"[NPU] 插件 {plugin.name} 无可用远程版本，但可能存在预发布版本")
                continue

        # 跳过被标记为跳过当前版本的插件
        if not skip_blacklist:
            remote_version_list = [
                i
                for i in remote_version_list
                if i
                not in [
                    j.version
                    for j in BLACK_LIST.plugins
                    if j.name == plugin.name and j.skip_type == SkipType.CURRENT
                ]
            ]
            if not remote_version_list:
                logger.info(f"[NPU] 插件 {plugin.name} 无可用远程版本，但可能存在被跳过的版本")
                continue

        remote_version = parse(remote_version_list[-1])
        if local_version < remote_version:
            result.plugins.append(
                PluginInfo(
                    name=plugin.name,
                    local_version=str(local_version),
                    remote_version=str(remote_version),
                    pre_release=remote_version.is_prerelease,
                )
            )
            logger.info(
                f"[NPU] 插件 {plugin.name} 有可用更新，本地版本 {local_version}，远程版本 {remote_version}"
            )
        else:
            logger.info(f"[NPU] 插件 {plugin.name} 当前已是最新版本 {local_version}")

    return result
