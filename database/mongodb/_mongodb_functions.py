import importlib
import os
from database.mongodb.update_guild_config._update_guild_config import update_guild_config

directory = os.path.dirname(os.path.abspath(__file__))
module_path = "database.mongodb."
skip_files = ["__init__.py", os.path.basename(__file__)]

functions = [name[:-3] for name in os.listdir(directory)
             if os.path.isfile(os.path.join(directory, name)) and not name in skip_files]


def mongodb_functions(self):
    setattr(self, "update_guild_config", update_guild_config)
    for function in functions:
        function_path = f"{module_path}{function}"
        imported_module = importlib.import_module(function_path)
        setattr(self, function, getattr(imported_module, function))
