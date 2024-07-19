def config(self, data):
    self.guilds.update_one({"id": data["id"]}, {
        "$set": {"config": data["config"]}})
    return {
        "status": "OK",
        "message": f"Updated guild configuration for {data['name']} ${data['id']}"
    }
