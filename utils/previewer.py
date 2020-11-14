import parser
import sys

sys.path.append("../")


def execute(query):
    return query


class Preview(parser.Lexer):
    def __init__(self) -> None:
        self.query = "PREVIEW DELETE FROM TABLE WHERE 51 % 17 = 0"

    def _replace_delete(self):
        return self.query.upper().replace("PREVIEW ", "").replace("DELETE", "SELECT")

    def to_be_deleted(self):
        return execute(self._replace_delete())
