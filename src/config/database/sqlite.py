from dotenv import dotenv_values
import sqlite3 as sql
from .. import config

conn = sql.connect(config["SQLITE_DB"])
db = conn.cursor()