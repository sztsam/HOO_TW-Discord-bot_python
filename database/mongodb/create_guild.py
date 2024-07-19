from database.id_generator import id_generator


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
