def find_guild(self, guild_id: str) -> list:
    options = {"guild_id": guild_id}
    return list(self.guilds.find(options))
