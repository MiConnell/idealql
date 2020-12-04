import json
import os
from typing import Optional
import sqlite3

import pandas as pd

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_connection(
    driver: str, file_location=__location__, credential_file="credentials.json"
):
    with open(os.path.join(file_location, credential_file)) as f:
        (credentials,) = [i for i in json.load(f) if i["driver"] == driver]
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


if __name__ == "__main__":
    pass
