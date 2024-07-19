from database.id_generator import id_generator


def add_cronjob_to_base_config(self, data):
    if not data["time"] or not data["type"]:
        return {"status": False}
    basic_cronjobs = self.base_config.find({"name": "basic_cronjobs"})[0]
    cron_data = self.sample["cron"]
    cron_data["cron_id"] = id_generator(1)
    cron_data["time"] = data["time"] if not data["time"] else cron_data["time"]
    cron_data["type"] = data["type"] if not data["type"] else cron_data["type"]
    cron_data["message"] = data["message"] if not data["message"] else cron_data["message"]
    cron_data["channel_id"] = data["channel_id"] if not data["channel_id"] else cron_data["channel_id"]
    cron_data["onetime"] = data["onetime"] if not data["onetime"] else cron_data["onetime"]
    cron_data["play"] = data["play"] if not data["play"] else cron_data["play"]
    basic_cronjobs["value"].append(cron_data)
    self.base_config.update_one({"name": "basic_cronjobs"}, {
                                "$set": {"value": basic_cronjobs["value"]}})
    return cron_data
