from slacker import Slacker
import json
from rollbot_func import *

# setting for rollbot
with open('./config.json', 'r') as f:
    config = json.load(f)
# config.json ref: https://mingrammer.com/ways-to-manage-the-configuration-in-python/


bot_user_token = config['DEFAULT']["BOT_USER_OAUTH_ACCESS_TOKEN"]
slack = Slacker(bot_user_token)
channels = ["#bots_test"]

for channel in channels:
    # initial test for rollbot
    post_to_channel(slack, channel, '안녕하세요? Roll Bot입니다🤖📘')
