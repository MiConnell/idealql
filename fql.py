from typing import Any, List
import keywords

kw = keywords.sql_keywords
fkw = keywords.fql_keywords
op = keywords.operators
comp = keywords.comparisons


class Error:
    def __init__(
        self, position_start: int, position_end: int, error_name: str, details: str
    ):
        self.position_start = position_start
        self.position_end = position_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        return f"{self.error_name}: {self.details}"


class Position:
    def __init__(
        self, idx: int, line: int, file_name: str, file_text: str
    ) -> None:
        self.idx = idx
        self.line = line
        self.file_name = file_name
        self.file_text = file_text

    def advance(self, word: str) -> Any:
        self.idx += 1
        self.line = self.line + 1 if word == "\n" else self.line

        return self

    def copy(self):
        ...


class Lexer:
    def __init__(self, file_name: str, file_text: str) -> None:
        self.file_name = file_name
        self.file_text = file_text
        self.position = Position(-1, 0, file_name, file_text)
        self.body: List[str] = self.file_text.split()
        self.clauses: List[str] = self.file_text.split(sep=',')
        self.word = self.body[self.position.idx]

    def advance(self):
        self.position.advance(self.word)
        self.word = self.body[self.position.idx]

    def discover_keywords(self):
        self.keyword_dict = {}
        for i, w in enumerate(self.body):
            if w == '*' and self.body[i - 1] == "SELECT":
                self.keyword_dict[(w, i)] = 'keyword'
            elif w in kw:
                self.keyword_dict[(w, i)] = 'keyword'
            elif w in fkw:
                self.keyword_dict[(w, i)] = 'fql_keyword'
            elif w in op:
                self.keyword_dict[(w, i)] = 'operator'
            elif w in comp:
                self.keyword_dict[(w, i)] = 'comparison'
            else:
                self.keyword_dict[(w, i)] = 'plain'
        return self.keyword_dict


TEST_TEXT = """EXCLUDING (COLUMN2) SELECT
 *, 10 * 10,
FROM TEST_TABLE
WHERE 1 = 1"""

lex = Lexer('fql.py', TEST_TEXT)
