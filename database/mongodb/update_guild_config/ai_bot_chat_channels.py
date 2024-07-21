def ai_bot_chat_channels(self, data: dict, action: str, guild: dict) -> str:
    ai_bot_chat_channels = guild["config"]["ai_bot_chat_channels"]
    match action:
        case "add":
            if not data.get("channel_id") in ai_bot_chat_channels:
                ai_bot_chat_channels.append(data["channel_id"])
                self.guilds.update_one({"guild_id": data["guild_id"]}, {
                    "$set": {"config.ai_bot_chat_channels": ai_bot_chat_channels}})
                return f"Channel {data['channel_id']} added to AI bot chat channels successfully"
            return f"Channel {data['channel_id']} is already in AI bot chat channels!"
        case "remove":
            if data.get("channel_id") in ai_bot_chat_channels:
                ai_bot_chat_channels.remove(data["channel_id"])
                self.guilds.update_one({"guild_id": data["guild_id"]}, {
                    "$set": {"config.ai_bot_chat_channels": ai_bot_chat_channels}})
                return f"Channel {data['channel_id']} removed from AI bot chat channels successfully"
            return f"Channel {data['channel_id']} is not in AI bot chat channels!"
        case _:
            return f"Error"
