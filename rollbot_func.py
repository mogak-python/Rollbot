# This file is lib. for functions of rollbot
# ref: https://hyesun03.github.io/2016/10/08/slackbot/


def post_to_channel(slack, channel, message):
    slack.chat.post_message(channel, message, as_user=True)
