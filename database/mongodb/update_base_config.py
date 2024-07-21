def update_base_config(self, type: str, data: str | dict | list | bool) -> dict:
    self.base_config.update_one({"name": type}, {"$set": {"value": data}})
    return {
        "status": "OK",
        "message": f"Updated base configuration: {type}"
    }
