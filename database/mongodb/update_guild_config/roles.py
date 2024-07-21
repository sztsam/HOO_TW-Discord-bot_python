import copy
from database.id_generator import id_generator


def roles(self, data: dict, action: str, guild: dict) -> None:
    role_data = next((role for role in guild["config"]["roles"]
                      if role["role_id"] == data["role_id"]), None)
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
            self.guilds.update_one({"guild_id": data["guild_id"]}, {"$set": {"config.roles": guild["config"]["roles"]}})
        case "delete":
            if not role_data:
                return
            guild["config"]["roles"].remove(role_data)
            self.guilds.update_one({"guild_id": data["guild_id"]}, {"$set": {"config.roles": guild["config"]["roles"]}})
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
            self.guilds.update_one({"guild_id": data["guild_id"]}, {"$set": {"config.roles": guild["config"]["roles"]}})
