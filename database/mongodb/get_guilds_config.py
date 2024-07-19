def get_guilds_config(self):
    return list(self.guilds.find({}))
