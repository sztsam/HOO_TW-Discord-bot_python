def find_guild(self, guild_id):
    options = {"guild_id": guild_id}
    return list(self.guilds.find(options))
