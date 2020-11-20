import argparse

from connections import connection
from utils import converter, parser, previewer

ps = argparse.ArgumentParser(description="Run FQL File.")
ps.add_argument(
    "file name", metavar="Filename", type=str, nargs=1, help=".fql file to run"
)
ps.add_argument("-c", "--credentials", help="set the connection file destination")
args = ps.parse_args()
conn = (
    connection.get_connection(creds)
    if (creds := args.credentials)
    else connection.get_connection()
)


class InvalidConnectionError(Exception):
    pass


class FQL:
    def __init__(self, ag):
        self.ag = ag
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
        return self


if __name__ == "__main__":
    reader = FQL(args)
    reader.initialize()
    reader.main()
