import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

# from nonebot_adapter_walleq import Adapter as Walleq_Adapter

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_plugin("nonebot_plugin_update")

if __name__ == "__main__":
    nonebot.run()
