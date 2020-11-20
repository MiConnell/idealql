import file_preprocessing as fp

from connections import connection
from utils import converter, parser, previewer

file_name = fp.file_name
conn = fp.conn
args = fp.args

class InvalidConnectionError(Exception):
    pass


class FQL:
    def __init__(self, argument):
        self.argument = argument
        self.query = " ".join(open(file_name, "r").read().split())
        return None

    def __repr__(self) -> str:
        return f"FQL Connection: {self.conn}"

    def initialize(self):
        try:
            self.conn = connection.SetConnection(*conn)
        except InvalidConnectionError:
            raise InvalidConnectionError(
                f"""credentials.json file not found in default location '{connection.__location__}'!

Either add the file there or set a new file name and location with --credentials (or -c)."""
            )

    def main(self):
        self.parse = parser.Lexer(str(file_name))
        self.convert = converter.ConvertSelect(self.parse.excluded_columns)
        self.preview = previewer.Preview(self.query)
        return self.preview.to_be_deleted()


if __name__ == "__main__":
    reader = FQL(args)
    reader.initialize()
    print(reader.main())
