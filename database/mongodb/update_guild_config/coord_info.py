def coord_info(self, data):
    self.guilds.update_one({"guild_id": data["guild_id"]}, {
        "$set": {"config.coord_info": data["coord_info"]}})
