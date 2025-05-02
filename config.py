import os

class Config(object):
    BOT_TOKEN = os.environ.get("7791056995:AAGTt6xsnHrcST6V496hzHlht1RpO-be1lc")
    API_ID = int(os.environ.get("28748671"))
    API_HASH = os.environ.get("f53ec7c41ce34e6d585674ed9ce6167c")
    VIP_USER = os.environ.get('VIP_USERS', '1169394017').split(',')
    VIP_USERS = [int(1169394017) for user_id in VIP_USER]
