import os
import importlib
from database.default_config.base_config.translations._translations import translations

directory = os.path.dirname(os.path.abspath(__file__))
module_path = "database.default_config.base_config."
skip_files = ["__init__.py", os.path.basename(__file__)]


def base_config():
    base_config = {}
    base_config["translations"] = translations()
    types = [name[:-3] for name in os.listdir(directory)
             if os.path.isfile(os.path.join(directory, name)) and not name in skip_files]
    for type in types:
        type_path = f"{module_path}{type}"
        imported_module = importlib.import_module(type_path)
        base_config[type] = getattr(imported_module, type)
    return base_config
