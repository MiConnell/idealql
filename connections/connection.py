import json
import os
from typing import Optional

import pandas as pd

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_connection(file_location=__location__):
    with open(os.path.join(file_location, "credentials.json")) as f:
        (credentials,) = json.load(f)
    return [v for v in credentials.values()]


class SetConnection:
    def __init__(
        self,
        driver: str,
        host: str,
        database: str,
        username: str,
        password: str,
        port: Optional[int] = 8000,
    ):
        self.driver = driver
        self.host = host
        self.database = database
        self.user = username
        self.password = password
        self.port = port


df = pd.DataFrame()

# TODO - connectors to
#      MySQL
#      Postgres
#      SQLite

"""
from connections import connection
driver = "sql server"
host = "192.168.1.1"
database = "PROD"
user = "SA"
password = "hunter2"
port = 8000

s = SetConnection(driver, host, database, user, password, port)
"""
