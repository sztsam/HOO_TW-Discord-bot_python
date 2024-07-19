def market(self, data):
    base_markets = self.get_base_config("markets")
    markets_array = [market["market"] for market in base_markets]
    if not data["market"] in markets_array:
        return
    self.guilds.update_one({"guild_id": data["guild_id"]}, {
        "$set": {"market": data["market"]}})
