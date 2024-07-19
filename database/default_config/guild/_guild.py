from database.default_config.guild.main import main
from database.default_config.guild.config import config


def guild():
    guild_config = main
    guild_config["config"] = config
    return guild_config
