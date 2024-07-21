def get_guilds_config(self) -> list:
    return list(self.guilds.find({}))
