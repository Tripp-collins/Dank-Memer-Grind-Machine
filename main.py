import discord
import asyncio
import yaml
import requests
import os

def loading_config():
  with open(r'C:\Users\User\Documents\Personal\Coding\DankGrinder (Python)\config.yml') as stream: 
    configuration = yaml.load(stream, Loader=yaml.FullLoader)
    token = configuration["instances"][0]["token"]
    channel_id = configuration["instances"][0]["channel_id"]
    is_master = configuration["instances"][0]["is_master"]
    shifts = configuration["shifts"]
    active_shift_length = shifts[0]["duration"]
    dormant_shift_length = shifts[1]["duration"]
    features = configuration["features"]
    commands = features["commands"]
    beg = commands["beg"]
    postmeme = commands["postmeme"]
    search = commands["search"]
    highlow = commands["highlow"]
    fish = commands["fish"]
    hunt = commands["hunt"]
    auto_sell = features["auto_sell"]
    auto_sell_enabled = auto_sell["enable"]
    auto_sell_items = auto_sell["items"]
    auto_buy = features["auto_buy"]

loading_config()
