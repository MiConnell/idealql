import argparse

import file_preprocessing as fp
from connections import connection
from utils import converter, parser, previewer

FILE_NAME = fp.file_name
CONN = fp.conn
ARGS = fp.args


class InvalidConnectionError(Exception):
    pass


class FQL:
    def __init__(self, argument: argparse.Namespace):
        self.argument = argument
        self.query = " ".join(open(FILE_NAME).read().split())
        return None

    def __repr__(self) -> str:
        return f"FQL Connection: {self.conn}"

    def initialize(self):
        try:
            self.conn = connection.SetConnection(*CONN)
        except InvalidConnectionError:
            raise InvalidConnectionError(
                f"""credentials.json file not found in default location '{connection.__location__}'!

Either add the file there or set a new file name and location with --credentials (or -c).""",
            )

    def main(self):
        self.parse = parser.Lexer(str(FILE_NAME))
        self.convert = converter.ConvertSelect(self.parse.excluded_columns)
        self.preview = previewer.Preview(self.query, self.conn)
        return self.preview.to_be_deleted()


if __name__ == "__main__":
    reader = FQL(ARGS)
    reader.initialize()
    reader.main()
