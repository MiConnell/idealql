import re
import sys
from typing import Any, List

sys.path.append("../")
from keywords import keywords


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
    def __init__(self, idx: int, line: int, file_name: str, file_text: str) -> None:
        self.idx = idx
        self.line = line
        self.file_name = file_name
        self.file_text = file_text

    def advance(self, word: str) -> Any:
        self.idx += 1
        self.line = self.line + 1 if word == "\n" else self.line

        return self

    def copy(self):
        self.elips = ...


class Lexer:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.file_text: str = self._preprocess(self.file_name)
        self.position = Position(-1, 0, self.file_name, self.file_text)
        self.body: List[str] = self.file_text.split()
        self.clauses: List[str] = self.file_text.split(sep=",")
        self.select: List[str] = self.file_text.split(
            sep="FROM",
        )
        self.word = self.body[self.position.idx]

    def _preprocess(self, file_name: str) -> str:
        self.file_name = file_name
        return " ".join(open(self.file_name, "r").read().split()).replace(",", "")

    def _char_tagger(self, char: str) -> str:
        self.char = char
        try:
            return keywords.kw_dict[self.char]
        except KeyError:
            if self.char.replace(".", "").isdigit():
                return "num"
            else:
                return "non_keyword"

    @property
    def excluded_columns(self) -> List[str]:
        self.query = self.file_text
        self.excols = "(?<=excluding)(.*)(?=select)"
        return "".join(re.findall(self.excols, self.query, re.IGNORECASE)).split()

    @property
    def from_table(self) -> str:
        # TODO add parsing for subqueries/multiple froms
        # for now will just use FROM even though this will need to be updated
        return self.body[self.body.index("FROM") + 1]

#   likely removing
    def advance(self):
        self.position.advance(self.word)
        self.word = self.body[self.position.idx]

    @property
    def discover_keywords(self):
        self.keyword_dict = {}
        for i, w in enumerate(self.body):
            tag = self._char_tagger(w)
            self.keyword_dict[(i, w)] = tag
        return self.keyword_dict
