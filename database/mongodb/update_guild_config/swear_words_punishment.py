def swear_words_punishment(self, data):
    self.guilds.update_one({"guild_id": data["guild_id"]}, {
        "$set": {"config.swear_words_punishment": data["swear_words_punishment"]}})
