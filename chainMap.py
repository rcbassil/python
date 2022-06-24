from collections import ChainMap


cmd_proxy = {}  # The user doesn't provide a proxy

local_proxy = {"proxy": "proxy.local.com"}

global_proxy = {"proxy": "proxy.global.com"}


config = ChainMap(cmd_proxy, local_proxy, global_proxy)

print(config["proxy"])


numbers = {"one": 1, "two": 2}

letters = {"a": "A", "b": "B"}


alpha_nums = ChainMap(numbers, letters)

print(alpha_nums)

alpha_nums.maps[1]["c"] = "C"

print(alpha_nums.items())

print(alpha_nums)


