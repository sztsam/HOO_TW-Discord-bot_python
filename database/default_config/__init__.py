from database.default_config.guild import guild
from database.default_config.base_config import base_config


def default_config():
    return {
        "guild": guild(),
        "base_config": base_config()
    }
