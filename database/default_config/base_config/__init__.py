import os
import importlib
from database.default_config.base_config.translations import translations

directory = "./database/default_config/base_config"


def base_config():
    imported_modules = {}
    base_config = {}
    base_config["translations"] = translations()
    types = [name for name in os.listdir(directory) if os.path.isfile(
        f"{directory}/{name}") and name != "__init__.py"]
    for type in types:
        imported_modules[type] = importlib.import_module(type[:-3], directory)
        base_config[type[:-3]
                    ] = getattr(imported_modules[type], type[:-3])
    return base_config
