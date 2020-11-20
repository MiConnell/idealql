import argparse
import os

from connections import connection
from utils import converter, parser, previewer

ps = argparse.ArgumentParser(description="Run FQL File.")
ps.add_argument(
    "file_name", metavar="Filename", type=str, nargs=1, help=".fql file to run"
)
ps.add_argument(
    "-c",
    "--credentials",
    help="set the connection file destination (drive name only, file must be named 'credentials.json')",
)
args = ps.parse_args()
creds = os.path.abspath(str(args.credentials))
file_name = os.path.abspath("".join(args.file_name))
conn = (
    connection.get_connection(creds)
    if args.credentials
    else connection.get_connection()
)


class InvalidConnectionError(Exception):
    pass


class FQL:
    def __init__(self, ag):
        self.ag = ag
        self.query = " ".join(
            open(file_name, "r").read().split())
        return None

    def __repr__(self) -> str:
        return f"FQL Connection: {self.conn}"

    def initialize(self):
        try:
            self.conn = connection.SetConnection(*conn)
        except FileNotFoundError:
            raise FileNotFoundError(
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
