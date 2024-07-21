from database.mongodb._mongodb_functions import MongodbFunctions
from database.default_config._default_config import default_config
import pymongo
import os
import dotenv

dotenv.load_dotenv()


class Database(MongodbFunctions):
    def __init__(self):
        self.main_db = "DISCORD_BOT_DATABASE"
        self.guilds = "GUILDS"
        self.base_config = "BASE_CONFIG"
        self.errors = "ERRORS"
        self.sample = default_config()
        setup_client(self)
        setup_database(self)
        super().__init__(self)


def setup_client(self):
    self.client = pymongo.MongoClient(os.environ.get("DISCORD_BOT_MONGODB_URI"))


def setup_database(self):
    self.main_db = self.client[f"{self.main_db}"]
    self.guilds = self.main_db[f"{self.guilds}"]
    self.base_config = self.main_db[f"{self.base_config}"]
    self.errors = self.main_db[f"{self.errors}"]
    if self.guilds.count_documents({}) < 1:
        self.guilds.insert_one(self.sample["guild"])
    if self.base_config.count_documents({}) < 1:
        temp_config = []
        temp_config.append({"name": "sample_guild", "value": self.sample["guild"]})
        for [key, value] in self.sample["base_config"].items():
            temp_config.append({"name": key, "value": value})
        self.base_config.insert_many(temp_config)
