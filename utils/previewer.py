import pandas as pd

from utils import parser


def execute(query: str, conn: str) -> str:
    df = pd.read_sql(query, con=conn)
    return df.to_string()


class Preview(parser.Lexer):
    def __init__(self, query: str, conn: str) -> None:
        self.query = query
        self.conn = conn

    def _replace_delete(self) -> str:
        return self.query.upper().replace("PREVIEW ", "").replace("DELETE", "SELECT *")

    def to_be_deleted(self) -> str:
        return execute(self._replace_delete(), self.conn)
