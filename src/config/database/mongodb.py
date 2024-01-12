from dotenv import dotenv_values
from pymongo import MongoClient
from .. import config
if config["MODE"] == "dev":
  client = MongoClient('localhost', 27017)
else:
  client = MongoClient(config["MONGODB_URI"])

db = client[config["DB_NAME"]]
