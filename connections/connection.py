from dataclasses import dataclass
import pandas as pd


@dataclass
class SetConnection:
    db: str

df = pd.DataFrame()

# TODO - connectors to
#      MySQL
#      Postgres
#      SQLite


"""
    from connections import connection
    connection.SetConnection(db = "mssql")
"""
