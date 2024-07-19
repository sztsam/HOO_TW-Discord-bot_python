def live_ennoblements(self, data):
    self.guilds.update_one({"guild_id": data["guild_id"]}, {
        "$set": {"config.live_ennoblements": data["live_ennoblements"]}})
