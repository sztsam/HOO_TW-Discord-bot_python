def guild_settings(self, data: dict) -> None:
    self.guilds.update_one({"guild_id": data["guild_id"]}, {
        "$set": {
            "pass": data["pass"],
            "active": data["active"],
            "market": data["market"],
            "preferred_language": data["preferred_language"],
            "global_world": data["global_world"],
            "global_guild": data["global_guild"]
        }
    })
