import os
import json

directory = "./database/default_config/base_config/translations"
translation_types = [name for name in os.listdir(f"{directory}")
                     if os.path.isdir(f"{directory}/{name}") and name != "__pycache__"]


def read_json_file(file_path):
    with open(file_path, 'r', encoding="utf-8",) as file:
        return json.load(file)


def translations():
    translations = {}
    for type in translation_types:
        translations[type] = {}
        langs = [lang for lang in os.listdir(
            f"{directory}/{type}")]
        for lang in langs:
            translations[type][lang[:2]] = read_json_file(
                f"{directory}/{type}/{lang}")
    return translations
