import argparse
import os

from connections import connection

# add argument parsing
ps = argparse.ArgumentParser(description="Run FQL File.")
ps.add_argument(
    "file_name",
    metavar="Filename",
    type=str,
    nargs=1,
    help=".fql file to run",
)
ps.add_argument(
    "-c",
    "--credentials",
    help="set the connection file destination (drive name only, file must be named 'credentials.json')",
)

ps.add_argument(
    "-d",
    "--driver",
    help="specify which driver to use",
)
args = ps.parse_args()

# define credentials
if not args.credentials:
    try:
        # default location
        creds = os.path.abspath(str(connection.__location__))
    except FileNotFoundError:
        raise FileNotFoundError(
            f"""credentials.json file not found in default location '{connection.__location__}'!
             Either add the file there or set a new file name and location with --credentials (or -c).""",
        )
else:
    try:
        # input credentials location
        creds = os.path.abspath(str(args.credentials))
    except FileNotFoundError:
        raise FileNotFoundError(f"'credentials.json' not found in '{args.credentials}'")

# get file name from input
file_name = os.path.abspath("".join(args.file_name))

# get connection properties based on credentials input or default
conn = (
    connection.get_connection(args.driver)
    if not args.credentials
    else connection.get_connection(creds)
)
