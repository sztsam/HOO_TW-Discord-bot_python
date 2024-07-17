import dotenv
import os
from mongodb import Mongodb
dotenv.load_dotenv()

DEV = True
BOT_TOKEN = os.environ.get(
    "DISCORDJS_DEV_BOT_TOKEN") if DEV else os.environ.get("DISCORDJS_BOT_TOKEN")
BOT_CLIENT_ID = os.environ.get(
    "DISCORDJS_DEV_BOT_CLIENT_ID") if DEV else os.environ.get("DISCORDJS_BOT_CLIENT_ID")
BOT_GUILD_ID = os.environ.get(
    "DISCORDJS_DEV_GUILD_ID") if DEV else os.environ.get("DISCORDJS_OWN_GUILD_ID")

mongodb = Mongodb()
