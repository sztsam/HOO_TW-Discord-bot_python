def get_base_config(self, type: str) -> str | dict | list | bool:
    options = {"_id": 0}
    match type:
        case "all":
            config = self.base_config.find({}, options)
            config_object = {}
            for item in config:
                config_object[item["name"]] = item["value"]
            return config_object
        case _:
            config = self.base_config.find({"name": type}, options)
            return config[0]["value"]
