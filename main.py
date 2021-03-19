import discord
import asyncio
import yaml
import requests
import os

def loading_config():
  stream = open(r'C:\Users\User\Documents\Personal\Coding\DankGrinder (Python)\config.yml')
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
  auto_buy_fishing_pole = auto_buy["fishing_pole"]
  auto_buy_hunting_rifle = auto_buy["hunting_rifle"]
  auto_buy_laptop = auto_buy["laptop"]
  auto_gift = features["auto_gift"]
  auto_gift_enabled = auto_gift["enable"]
  auto_gift_items = auto_gift["items"]
  auto_share = features["auto_share"]
  auto_share_enabled = auto_share["enable"]
  auto_share_maximum_balance = auto_share["maximum_balance"]
  auto_share_minimum_balance = auto_share["minumum_balance"]
  auto_bet = features["auto_bet"]
  auto_bet_enabled = auto_bet["enable"]
  auto_bet_pause_below_balance = auto_bet["pause_below_balance"]
  auto_tidepod = features["auto_tidepod"]
  auto_tidepod_enabled = auto_tidepod["enable"]
  auto_tidepod_buy_lifesaver_on_death = auto_tidepod["buy_lifesaver_on_death"]
  balance_check = features["balance_check"]
  balance_check_enabled = balance_check["enable"]
  balance_check_interval = balance_check["interval"]
  compatibility = configuration["compatibility"]
  compatibility_postmeme = compatibility["postmeme"]
  compatibility_allowed_searches = compatibility["allowed_searches"]
  compatibility_search_cancel = compatibility["search_cancel"]
  compatibility_cooldown = compatibility["cooldown"]
  compatibility_cooldown_beg = compatibility_cooldown["beg"]
  compatibility_cooldown_search = compatibility_cooldown["search"]


loading_config()
