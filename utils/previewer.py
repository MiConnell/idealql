from utils import parser

def execute(query):
    return query


class Preview(parser.Lexer):
    def __init__(self, query) -> None:
        self.query = query

    def _replace_delete(self):
        return self.query.upper().replace("PREVIEW ", "").replace("DELETE", "SELECT *")

    def to_be_deleted(self):
        return execute(self._replace_delete())
