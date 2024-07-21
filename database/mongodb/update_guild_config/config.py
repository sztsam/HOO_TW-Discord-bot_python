def config(self, data: dict) -> dict:
    self.guilds.update_one({"id": data.get("id")}, {"$set": {"config": data.get("config")}})
    return {
        "status": "OK",
        "message": f"Updated guild configuration for {data.get('name')} ${data.get('id')}"
    }
