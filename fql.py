from typing import List
import keywords

kw = keywords.keywords


class Lexer:
    def __init__(self, text: str = "", position: int = 0):
        self.text = text
        self.position = position
        self.body: List[str] = self.text.split()
        self.word = self.body[self.position]

    def advance(self):
        self.position += 1
        self.word = self.body[self.position]

    def discover_keywords(self):
        self.keyword_list = [w for w in self.body if w in kw]
        return self.keyword_list
