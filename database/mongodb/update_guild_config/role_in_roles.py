def role_in_roles(self, data: dict, action: str, guild: dict) -> None:
    role_in_roles_data = next((role for role in guild["config"]["roles"]
                               if role["message_id"] == data["message_id"]), None)
    if not role_in_roles_data:
        return
    role_in_roles = next((role for role in role_in_roles_data["roles"]
                          if role["role_id"] == data["role_id"]), None)
    match action:
        case "add":
            if role_in_roles:
                return
            base_role_in_roles_data = self.get_base_config("role_in_roles")
            base_role_in_roles_data["role_name"] = data["role_name"]
            base_role_in_roles_data["emoji_id"] = data["emoji_id"]
            base_role_in_roles_data["role_id"] = data["role_id"]
            role_in_roles_data["roles"].append(base_role_in_roles_data)
            self.guilds.update_one({"guild_id": data["guild_id"]}, {"$set": {"config.roles": guild["config"]["roles"]}})
        case "delete":
            if not role_in_roles:
                return
            role_in_roles_data["roles"].remove(role_in_roles)
            self.guilds.update_one({"guild_id": data["guild_id"]}, {"$set": {"config.roles": guild["config"]["roles"]}})
        case "modify":
            if not role_in_roles:
                return
            if len(data["role_name"]) > 0:
                role_in_roles["role_name"] = data["role_name"]
            if len(data["emoji_id"]) > 0:
                role_in_roles["emoji_id"] = data["emoji_id"]
            if len(data["role_id"]) > 0:
                role_in_roles["role_id"] = data["role_id"]
            self.guilds.update_one({"guild_id": data["guild_id"]}, {"$set": {"config.roles": guild["config"]["roles"]}})
