def active(self, data):
    if not isinstance(data["active"], bool):
        return
    self.guilds.update_many({"guild_id": data["guild_id"]}, {
                            "$set": {"active": data["active"]}})
    print(
        f"{'Activated' if data['active'] else 'Deactivated'} [{data['guild_id']}]: {data['guild_name']}")
