from database.id_generator import id_generator


def cronjobs(self, data, action, guild):
    cron_data = next((
        cron for cron in guild["config"]["cronjobs"] if cron["cron_id"] == data["cron_id"]), None)
    cron_keys = ["cron_id", "time", "type",
                 "message", "channel_id", "onetime", "play"]
    match action:
        case "start":
            if not cron_data:
                return
            cron_data["start"] = True
            self.guilds.update_one({"guild_id": data["guild_id"]}, {
                "$set": {"config.cronjobs": guild["config"]["cronjobs"]}})
        case "stop":
            if not cron_data:
                return
            cron_data["start"] = False
            self.guilds.update_one({"guild_id": data["guild_id"]}, {
                "$set": {"config.cronjobs": guild["config"]["cronjobs"]}})
        case "create":
            if not data["time"] or not data["type"] or not data["channel_id"]:
                return
            base_cronjobs_data = self.get_base_config("cron")
            base_cronjobs_data["cron_id"] = id_generator(1)
            base_cronjobs_data["time"] = data["time"]
            base_cronjobs_data["type"] = data["type"]
            base_cronjobs_data["message"] = data["message"] if len(
                str(data["message"])) else base_cronjobs_data["message"]
            base_cronjobs_data["channel_id"] = data["channel_id"]
            base_cronjobs_data["onetime"] = data["onetime"] if len(
                data["onetime"]) else base_cronjobs_data["onetime"]
            base_cronjobs_data["play"] = data["play"] if len(
                str(data["play"])) else base_cronjobs_data["play"]
            guild["config"]["cronjobs"].append(base_cronjobs_data)
            self.guilds.update_one({"guild_id": data["guild_id"]}, {
                "$set": {"config.cronjobs": guild["config"]["cronjobs"]}})
            return base_cronjobs_data
        case "delete":
            if not cron_data:
                return
            guild["config"]["cronjobs"].remove(cron_data)
            self.guilds.update_one({"guild_id": data["guild_id"]}, {
                "$set": {"config.cronjobs": guild["config"]["cronjobs"]}})
        case "modify":
            if not cron_data:
                return
            for key in cron_keys:
                if len(data[key]) > 0:
                    cron_data[key] = data[key]
            self.guilds.update_one({"guild_id": data["guild_id"]}, {
                "$set": {"config.cronjobs": guild["config"]["cronjobs"]}})
            return cron_data
