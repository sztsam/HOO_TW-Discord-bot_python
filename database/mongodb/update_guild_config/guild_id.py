def guild_id(self, data):
    if not data["new_guild_id"]:
        return
    self.guilds.update_one({"guild_id": data["guild_id"]}, {
        "$set": {"guild_id": data["new_guild_id"]}})
