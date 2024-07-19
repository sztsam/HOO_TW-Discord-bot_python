def get_guild_data(self, id, password):
    options = {
        "guild_id": id,
        "pass": password
    }
    found_guild = self.guilds.find_one(options)
    return {
        "status": "OK" if found_guild else "ERROR",
        "guild_id": found_guild["guild_id"] if found_guild else None,
        "pass": found_guild["pass"] if found_guild else None,
        "market": found_guild["market"] if found_guild else None,
        "config": found_guild["config"] if found_guild else None
    }
