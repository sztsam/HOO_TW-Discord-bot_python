def market(self, data: dict) -> None:
    base_markets = self.get_base_config("markets")
    markets_array = [market["market"] for market in base_markets]
    if not data.get("market") in markets_array:
        return
    self.guilds.update_one({"guild_id": data["guild_id"]}, {"$set": {"market": data["market"]}})
