from connections.connection import SetConnection

from utils import converter, parser, previewer
from connections import connection

conn = [
    'mssql',
    'localhost',
    'dbname',
    'sa',
    'someThingComplicated1234'
]


class FQL:
    def __init__(self):
        return None

    def __repr__(self) -> str:
        return f'FQL Connection: {self.conn}'

    def initialize(self, conn):
        self.conn = connection.SetConnection(*conn)

    def main(self):
        return self

if __name__ == "__main__":
    reader = FQL()
    reader.main()


f = FQL()
f.initialize(conn)

print(f)
