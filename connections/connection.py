from dataclasses import dataclass
from typing import Optional

import pandas as pd


@dataclass
class SetConnection:
    driver: str
    host: str
    database: str
    user: str
    password: str
    port: Optional[int] = 8000


df = pd.DataFrame()

# TODO - connectors to
#      MySQL
#      Postgres
#      SQLite

driver = "sql server"
host = "192.168.1.1"
database = "PROD"
user = "SA"
password = "hunter2"
port = 8000

s = SetConnection(driver, host, database, user, password, port)
