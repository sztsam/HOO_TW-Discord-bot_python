def password(self, data: dict) -> None:
    if not data.get("pass") or len(data["pass"]) < 6:
        return
    self.guilds.update_one({"guild_id": data["guild_id"]}, {"$set": {"pass": data["pass"]}})
