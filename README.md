<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-update

_✨ 用于检测 Nonebot 插件更新的 Nonebot 插件 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-update.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-update">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-update.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

欢迎使用 Nonebot 插件管家，本次启动用时 0.0001 秒，你有 1 个插件可以更新。

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-update

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-update

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-update

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-update

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-update

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_update"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

|        配置项        | 必填 | 默认值 |        说明        |
| :------------------: | :--: | :----: | :----------------: |
|    npu_auto_check    |  否  |  True  |  是否启用自动更新  |
| npu_check_prerelease |  否  | False  | 是否检测预览版更新 |

## 🎉 使用

### 指令表

|    指令    | 权限 | 需要@ | 范围 |               说明               |
| :--------: | :--: | :---: | :--: | :------------------------------: |
| /npu check | 主人 |  否   | 均可 | 手动检查更新，将使预览版始终启用 |

### 效果图
