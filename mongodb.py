import traceback
import dotenv
import os
import pymongo
import uuid
import datetime
from db_default_config import db_sample
dotenv.load_dotenv()


class Module:
    def __init__(self):
        self.client = pymongo.MongoClient(
            os.environ.get("DISCORD_BOT_MONGODB_URI"))
        self.main_db = "DISCORD_BOT_DATABASE"
        self.guilds = "GUILDS"
        self.base_config = "BASE_CONFIG"
        self.errors = "ERRORS"
        self.sample = db_sample
        self.setup_database()

    def check_connect(self):
        try:
            return self.client.admin.command('ping')["ok"]
        except Exception as error:
            print(f"Connection error: {error}")
            return False

    def close(self):
        self.client.close()

    def setup_database(self):
        self.main_db = self.client[f"{self.main_db}"]
        self.guilds = self.main_db[f"{self.guilds}"]
        self.base_config = self.main_db[f"{self.base_config}"]
        self.errors = self.main_db[f"{self.errors}"]
        if self.guilds.count_documents({}) < 1:
            self.guilds.insert_one(self.sample["guild"])
        if self.base_config.count_documents({}) < 1:
            temp_config = []
            temp_config.append(
                {"name": "sample_guild", "value": self.sample["guild"]})
            for [key, value] in self.sample["base_config"].items():
                temp_config.append({"name": key, "value": value})
            self.base_config.insert_many(temp_config)

    def get_base_config(self, type):
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

    def get_guilds_config(self):
        return list(self.guilds.find({}))

    def update_base_config(self, type, data):
        self.base_config.update_one({"name": type}, {"$set": {"value": data}})
        return {
            "status": "OK",
            "message": f"Updated base configuration: {type}"
        }

    def add_cronjob_to_base_config(self, data):
        if not data["time"] or not data["type"]:
            return {"status": False}
        basic_cronjobs = self.base_config.find({"name": "basic_cronjobs"})[0]
        cron_data = self.sample["cron"]
        cron_data["cron_id"] = str(uuid.uuid1)[:-13].replace("-", "")
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

    def find_guild(self, guild_id):
        options = {"guild_id": guild_id}
        return list(self.guilds.find(options))

    def create_guild(self, data):
        guild_exist = len(self.find_guild(data["guild_id"]))
        if guild_exist:
            errors = []
            if not data["guild_id"]:
                errors.append("Guild ID error")
            if not data["market"]:
                errors.append("Market error")
            if len(errors):
                return {
                    "status": "error",
                    "message": errors
                }

            new_data = self.get_base_config("sample_guild")
            new_data["id"] = str(uuid.uuid1)[:-13].replace("-", "")
            new_data["guild_id"] = data["guild_id"]
            new_data["name"] = data["name"]
            new_data["pass"] = data["pass"] if (data["pass"] and len(
                data["pass"]) > 4) else str(uuid.uuid4)[:-13].replace("-", "")
            new_data["market"] = data["market"][:2]
            self.guilds.insert_one(new_data)
            return {
                "status": "OK",
                "message": {
                    "status": "Guild created successfully",
                    "pass": new_data["pass"]
                }
            }
        else:
            self.active(data)
            return {
                "status": "OK",
                "message": "Guild already exist / reactivated successfully"
            }

    def ban(self, data):
        if (not isinstance(data["ban"], bool)) or (data["user"]["username"] != os.environ.get("DISCORD_BOT_ADMIN")):
            return
        self.guilds.update_many({"guild_id": data["guild_id"]}, {
                                "$set": {"ban": data["ban"], "ban_reason": data["reason"]}})
        print(
            f"{'Banned' if data['ban'] else 'Unbanned'} [{data['guild_id']} - {data['guild_name']}]: {data['reason']}")

    def active(self, data):
        if not isinstance(data["active"], bool):
            return
        self.guilds.update_many({"guild_id": data["guild_id"]}, {
                                "$set": {"active": data["active"]}})
        print(
            f"{'Activated' if data['active'] else 'Deactivated'} [{data['guild_id']}]: {data['guild_name']}")

    def get_guild_data(self, id, password):
        options = {
            "guild_id": id,
            "pass": password
        }
        found_guild = self.guilds.find_one(options)
        return {
            "status": "OK" if found_guild else "ERROR",
            "guild_id": found_guild["guild_id"] if found_guild else None,
            "pass": found_guild["pass"] if found_guild else None,
            "market": found_guild["market"] if found_guild else None,
            "config": found_guild["config"] if found_guild else None
        }

    def error_handling(self, error: Exception, parameters=None):
        error_message = str(error)
        error_stack = traceback.format_exc()
        error_stack_partial = error_stack.split('\n')[1]
        error_hash = f"{error_message}-{error_stack_partial}"
        existing_error = self.errors.find_one({"hash": error_hash})
        skip_error = {
            "startsWith": ["connect"],
            "includes": ["AxiosError: Request failed"]
        }
        if any(error_hash.startswith(string) for string in skip_error["startsWith"]):
            return False
        if any(string in error_hash for string in skip_error["includes"]):
            return False

        if not existing_error:
            data = {
                "ticket_status": "created",
                "comment": "",
                "hash": error_hash,
                "message": error_message,
                "parameters": parameters,
                "stack": error_stack,
                "count": 1,
                "timestamp": datetime.datetime.now(),
            }
            result = self.errors.insert_one(data)
        else:
            self.errors.update_one(
                {"hash": error_hash},
                {"$inc": {"count": 1}}
            )
        return False if existing_error else {"id": result.inserted_id, "hash": error_hash}
