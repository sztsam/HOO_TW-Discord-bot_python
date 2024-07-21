# module
from database.mongodb.active import active
from database.mongodb.add_cronjob_to_base_config import add_cronjob_to_base_config
from database.mongodb.ban import ban
from database.mongodb.check_connect import check_connect
from database.mongodb.close import close
from database.mongodb.create_guild import create_guild
from database.mongodb.error_handling import error_handling
from database.mongodb.find_guild import find_guild
from database.mongodb.get_base_config import get_base_config
from database.mongodb.get_guild_data import get_guild_data
from database.mongodb.get_guilds_config import get_guilds_config
from database.mongodb.update_base_config import update_base_config
# package
from database.mongodb.update_guild_config._update_guild_config import update_guild_config

import importlib
import os
import types


directory = os.path.dirname(os.path.abspath(__file__))
module_path = "database.mongodb."
skip_files = ["__init__.py", os.path.basename(__file__)]

static_functions = ["update_guild_config"]
dynamic_functions = [name[:-3] for name in os.listdir(directory)
                     if os.path.isfile(os.path.join(directory, name)) and not name in skip_files]
functions = static_functions + dynamic_functions


class MongodbFunctions():
    def __init__(self, __self):
        self.__self = __self

    # modules
    def active(self, data: dict) -> None:
        return active(self.__self, data)

    def add_cronjob_to_base_config(self, data: dict) -> dict:
        return add_cronjob_to_base_config(self.__self, data)

    def ban(self, data: dict) -> None:
        return ban(self.__self, data)

    def check_connect(self) -> bool:
        return check_connect(self.__self)

    def close(self) -> None:
        return close(self.__self)

    def create_guild(self, data: dict) -> dict:
        return create_guild(self.__self, data)

    def error_handling(self, error: Exception, parameters: dict | None = None) -> dict | bool:
        return error_handling(self.__self, error, parameters)

    def find_guild(self, guild_id: str) -> list:
        return find_guild(self.__self, guild_id)

    def get_base_config(self, type: str) -> str | dict | list | bool:
        return get_base_config(self.__self, type)

    def get_guild_data(self, id: str, password: str) -> dict:
        return get_guild_data(self.__self, id, password)

    def get_guilds_config(self) -> list:
        return get_guilds_config(self.__self)

    def update_base_config(self, type: str, data: str | dict | list | bool) -> dict:
        return update_base_config(self.__self, type, data)

    # package
    def update_guild_config(self, type: str, data: dict, action: str) -> dict | str | None:
        return update_guild_config(self.__self, type, data, action)


# dynamic import
# not used


def _mongodb_functions(self):
    for function in static_functions:
        bound_function = types.MethodType(eval(function), self)
        setattr(self, function, bound_function)

    for function in dynamic_functions:
        function_path = f"{module_path}{function}"
        imported_module = importlib.import_module(function_path)
        bound_function = types.MethodType(getattr(imported_module, function), self)
        setattr(self, function, bound_function)
