def coord_info(self, data: dict) -> None:
    self.guilds.update_one({"guild_id": data.get("guild_id")}, {"$set": {"config.coord_info": data.get("coord_info")}})
