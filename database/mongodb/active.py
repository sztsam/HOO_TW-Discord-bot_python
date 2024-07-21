def active(self, data: dict) -> None:
    if not isinstance(data.get("active"), bool):
        return
    self.guilds.update_many({"guild_id": data.get("guild_id")}, {"$set": {"active": data.get("active")}})
    print(f"{'Activated' if data.get('active') else 'Deactivated'} [{data.get('guild_id')}]: {data.get('guild_name')}")
