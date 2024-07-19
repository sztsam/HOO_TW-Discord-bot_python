import os


def ban(self, data):
    if (not isinstance(data["ban"], bool)) or (data["user"]["username"] != os.environ.get("DISCORD_BOT_ADMIN")):
        return
    self.guilds.update_many({"guild_id": data["guild_id"]}, {
                            "$set": {"ban": data["ban"], "ban_reason": data["reason"]}})
    print(
        f"{'Banned' if data['ban'] else 'Unbanned'} [{data['guild_id']} - {data['guild_name']}]: {data['reason']}")
