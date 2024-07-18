import traceback
import dotenv
import os
import pymongo
import datetime
import copy
from database.default_config import default_config
from database.id_generator import id_generator
dotenv.load_dotenv()


class Mongodb:
    def __init__(self):
        self.client = pymongo.MongoClient(
            os.environ.get("DISCORD_BOT_MONGODB_URI"))
        self.main_db = "DISCORD_BOT_DATABASE"
        self.guilds = "GUILDS"
        self.base_config = "BASE_CONFIG"
        self.errors = "ERRORS"
        self.sample = default_config()
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

    def find_guild(self, guild_id):
        options = {"guild_id": guild_id}
        return list(self.guilds.find(options))

    def create_guild(self, data):
        guild_exist = len(self.find_guild(data["guild_id"]))
        if not guild_exist:
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
            new_data["id"] = id_generator(1)
            new_data["guild_id"] = data["guild_id"]
            new_data["name"] = data["name"]
            new_data["pass"] = data["pass"] if (data["pass"] and len(
                data["pass"]) > 4) else id_generator(4)
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

    def update_guild_config(self, type, data, action):
        guild = self.find_guild(data["guild_id"])[0]
        if not guild:
            guild_created = self.create_guild(data)
            if guild_created["status"] == "error":
                return {
                    "status": "error",
                    "message": guild_created["message"]
                }
            else:
                guild = self.find_guild(data["guild_id"])[0]
        if guild["ban"]:
            return {
                "status": "error",
                "message": "Guild is banned"
            }

        match type:
            case "config":
                self.guilds.update_one({"id": data["id"]}, {
                                       "$set": {"config": data["config"]}})
                return {
                    "status": "OK",
                    "message": f"Updated guild configuration for {data['name']} ${data['id']}"
                }
            case "guild_settings":
                self.guilds.update_one({"guild_id": data["guild_id"]}, {
                    "$set": {
                        "pass": data["pass"],
                        "active": data["active"],
                        "market": data["market"],
                        "preferred_language": data["preferred_language"],
                        "global_world": data["global_world"],
                        "global_guild": data["global_guild"]
                    }
                })
            case "guild_id":
                if not data["new_guild_id"]:
                    return
                self.guilds.update_one({"guild_id": data["guild_id"]}, {
                    "$set": {"guild_id": data["new_guild_id"]}})
            case "pass":
                if not data["pass"] or len(data["pass"]) < 6:
                    return
                self.guilds.update_one({"guild_id": data["guild_id"]}, {
                    "$set": {"pass": data["pass"]}})
            case "market":
                base_markets = self.get_base_config("markets")
                markets_array = [market["market"] for market in base_markets]
                if not data["market"] in markets_array:
                    return
                self.guilds.update_one({"guild_id": data["guild_id"]}, {
                    "$set": {"market": data["market"]}})
            case "swear_words_punishment":
                self.guilds.update_one({"guild_id": data["guild_id"]}, {
                    "$set": {"config.swear_words_punishment": data["swear_words_punishment"]}})
            case "live_ennoblements":
                self.guilds.update_one({"guild_id": data["guild_id"]}, {
                    "$set": {"config.live_ennoblements": data["live_ennoblements"]}})
            case "coord_info":
                self.guilds.update_one({"guild_id": data["guild_id"]}, {
                    "$set": {"config.coord_info": data["coord_info"]}})
            case "ai_bot_chat_channels":
                ai_bot_chat_channels = guild["config"]["ai_bot_chat_channels"]
                match action:
                    case "add":
                        if not data["channel_id"] in ai_bot_chat_channels:
                            ai_bot_chat_channels.append(data["channel_id"])
                            self.guilds.update_one({"guild_id": data["guild_id"]}, {
                                "$set": {"config.ai_bot_chat_channels": ai_bot_chat_channels}})
                            return f"Channel {data['channel_id']} added to AI bot chat channels successfully"
                        return f"Channel {data['channel_id']} is already in AI bot chat channels!"
                    case "remove":
                        if data["channel_id"] in ai_bot_chat_channels:
                            ai_bot_chat_channels.remove(data["channel_id"])
                            self.guilds.update_one({"guild_id": data["guild_id"]}, {
                                "$set": {"config.ai_bot_chat_channels": ai_bot_chat_channels}})
                            return f"Channel {data['channel_id']} removed from AI bot chat channels successfully"
                        return f"Channel {data['channel_id']} is not in AI bot chat channels!"
            case "roles":
                role_data = next((
                    role for role in guild["config"]["roles"] if role["role_id"] == data["role_id"]), None)
                match action:
                    case "create":
                        if not data["channel_id"] or not data["message_id"] or not data["type"]:
                            return
                        base_roles_data = self.get_base_config("roles")
                        base_roles_data["role_id"] = id_generator(1)
                        base_roles_data["channel_id"] = data["channel_id"]
                        base_roles_data["message_id"] = data["message_id"]
                        base_roles_data["type"] = data["type"]
                        guild["config"]["roles"].append(base_roles_data)
                        self.guilds.update_one({"guild_id": data["guild_id"]}, {
                            "$set": {"config.roles": guild["config"]["roles"]}})
                    case "delete":
                        if not role_data:
                            return
                        guild["config"]["roles"].remove(role_data)
                        self.guilds.update_one({"guild_id": data["guild_id"]}, {
                            "$set": {"config.roles": guild["config"]["roles"]}})
                    case "modify":
                        if not role_data:
                            return
                        role_data_copy = copy.deepcopy(role_data)
                        guild["config"]["roles"].remove(role_data)
                        if len(data["channel_id"]) > 0:
                            role_data_copy["channel_id"] = data["channel_id"]
                        if len(data["message_id"]) > 0:
                            role_data_copy["message_id"] = data["message_id"]
                        if len(data["type"]) > 0:
                            role_data_copy["type"] = data["type"]
                        guild["config"]["roles"].append(role_data_copy)
                        self.guilds.update_one({"guild_id": data["guild_id"]}, {
                            "$set": {"config.roles": guild["config"]["roles"]}})
            case "role_in_roles":
                role_in_roles_data = next((
                    role for role in guild["config"]["roles"] if role["message_id"] == data["message_id"]), None)
                if not role_in_roles_data:
                    return
                role_in_roles = next((
                    role for role in role_in_roles_data["roles"] if role["role_id"] == data["role_id"]), None)
                match action:
                    case "add":
                        if role_in_roles:
                            return
                        base_role_in_roles_data = self.get_base_config(
                            "role_in_roles")
                        base_role_in_roles_data["role_name"] = data["role_name"]
                        base_role_in_roles_data["emoji_id"] = data["emoji_id"]
                        base_role_in_roles_data["role_id"] = data["role_id"]
                        role_in_roles_data["roles"].append(
                            base_role_in_roles_data)
                        self.guilds.update_one({"guild_id": data["guild_id"]}, {
                            "$set": {"config.roles": guild["config"]["roles"]}})
                    case "delete":
                        if not role_in_roles:
                            return
                        role_in_roles_data["roles"].remove(role_in_roles)
                        self.guilds.update_one({"guild_id": data["guild_id"]}, {
                            "$set": {"config.roles": guild["config"]["roles"]}})
                    case "modify":
                        if not role_in_roles:
                            return
                        if len(data["role_name"]) > 0:
                            role_in_roles["role_name"] = data["role_name"]
                        if len(data["emoji_id"]) > 0:
                            role_in_roles["emoji_id"] = data["emoji_id"]
                        if len(data["role_id"]) > 0:
                            role_in_roles["role_id"] = data["role_id"]
                        self.guilds.update_one({"guild_id": data["guild_id"]}, {
                            "$set": {"config.roles": guild["config"]["roles"]}})
            case "cronjobs":
                cron_data = next((
                    cron for cron in guild["config"]["cronjobs"] if cron["cron_id"] == data["cron_id"]), None)
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
                        if len(data["time"]) > 0:
                            cron_data["time"] = data["time"]
                        if len(data["type"]) > 0:
                            cron_data["type"] = data["type"]
                        if len(data["message"]) > 0:
                            cron_data["message"] = data["message"]
                        if len(data["channel_id"]) > 0:
                            cron_data["channel_id"] = data["channel_id"]
                        if len(data["onetime"]) > 0:
                            cron_data["onetime"] = data["onetime"]
                        if len(data["play"]) > 0:
                            cron_data["play"] = data["play"]
                        self.guilds.update_one({"guild_id": data["guild_id"]}, {
                            "$set": {"config.cronjobs": guild["config"]["cronjobs"]}})
                        return cron_data
