from utils import parser


def execute(query: str) -> str:
    return query


class Preview(parser.Lexer):
    def __init__(self, query: str) -> None:
        self.query = query

    def _replace_delete(self) -> str:
        return self.query.upper().replace("PREVIEW ", "").replace("DELETE", "SELECT *")

    def to_be_deleted(self) -> str:
        return execute(self._replace_delete())
