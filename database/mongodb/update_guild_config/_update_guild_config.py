import os
import importlib
import inspect

directory = os.path.dirname(os.path.abspath(__file__))
module_path = "database.mongodb.update_guild_config."
skip_files = ["__init__.py", os.path.basename(__file__)]
types = [type[:-3] for type in os.listdir(directory)
         if not type in skip_files and os.path.isfile(os.path.join(directory, type))]


def update_guild_config(self, type: str, data: dict, action: str) -> dict | str | None:
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
        case type if type in types:
            type_path = f"{module_path}{type}"
            module = importlib.import_module(type_path)
            function = getattr(module, type)
            function_inspect = inspect.signature(function)
            function_parameters_list = list(function_inspect.parameters.keys())
            parameters_to_pass = [eval(parameter) for parameter in function_parameters_list]
            function(*parameters_to_pass)
