import os
import json

directory = os.path.dirname(os.path.abspath(__file__))
skip_dir = ["__pycache__"]
translation_types = [name for name in os.listdir(f"{directory}")
                     if os.path.isdir(f"{directory}/{name}") and not name in skip_dir]


def read_json_file(file_path):
    with open(file_path, 'r', encoding="utf-8",) as file:
        return json.load(file)


def translations():
    translations = {}
    for type in translation_types:
        translations[type] = {}
        langs = [lang for lang in os.listdir(os.path.join(directory, type))]
        for lang in langs:
            translations[type][lang[:2]] = read_json_file(os.path.join(directory, type, lang))
    return translations
