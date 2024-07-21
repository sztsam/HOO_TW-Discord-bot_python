from database.id_generator import id_generator


def add_cronjob_to_base_config(self, data: dict) -> dict:
    if not data.get("time") or not data.get("type"):
        return {"status": False}
    basic_cronjobs = self.base_config.find({"name": "basic_cronjobs"})[0]
    cron_data: dict = self.sample["cron"]
    cron_data["cron_id"] = id_generator(1)
    cron_data["time"] = data.get("time") if not data.get("time") else cron_data.get("time")
    cron_data["type"] = data.get("type") if not data.get("type") else cron_data.get("type")
    cron_data["message"] = data.get("message") if not data.get("message") else cron_data.get("message")
    cron_data["channel_id"] = data.get("channel_id") if not data.get("channel_id") else cron_data.get("channel_id")
    cron_data["onetime"] = data.get("onetime") if not data.get("onetime") else cron_data.get("onetime")
    cron_data["play"] = data.get("play") if not data.get("play") else cron_data.get("play")
    basic_cronjobs["value"].append(cron_data)
    self.base_config.update_one({"name": "basic_cronjobs"}, {"$set": {"value": basic_cronjobs["value"]}})
    return cron_data
