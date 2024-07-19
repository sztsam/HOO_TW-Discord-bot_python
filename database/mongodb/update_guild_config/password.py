def password(self, data):
    if not data["pass"] or len(data["pass"]) < 6:
        return
    self.guilds.update_one({"guild_id": data["guild_id"]}, {
        "$set": {"pass": data["pass"]}})
