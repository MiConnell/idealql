from utils import parser
import re
from typing import List

import pandas as pd
from connections import connection

df = pd.DataFrame()

query_file = "queries/queries.fql"

lex = parser.Lexer(query_file)

# This is just here so no errors are raised
def execute(query: str) -> List[str]:
    query = query
    return ["COLUMN3", "COLUMN4"]

conn = connection
# Carry on


class ConvertSelect:
    """
    EXCLUDING COLUMN4 SELECT * FROM _TABLE_
    ->
    SELECT COLUMN1, COLUMN2, COLUMN3, COLUMN5 FROM _TABLE_
    """
    def __init__(self, excluded_columns: List[str]) -> None:
        self.excluded_columns = excluded_columns
        if self.excluded_columns is not None:
            self.other_columns = self._included_columns(self.excluded_columns)

    # get all columns except excluded from database
    def _included_columns(self, excluded_columns: List[str]) -> None:
        self.inclusive_select_statement = f"""
                SELECT COLUMN_NAME FROM
                INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = {lex.from_table}
                AND COLUMN_NAME NOT IN
                ({", ".join(excluded_columns)})
        """
        self.included_columns = execute(
            self.inclusive_select_statement
        )  # need to actually run the query

    # take columns from _included_columns and replace * in SELECT with those columns
    def inclusive_select(self) -> str:
        self.exc_select_statement: str = lex.file_text.replace(
            "*", ", ".join(iter(self.included_columns))
        )
        presel = "(?<=select).*"
        return f'SELECT{"".join(re.findall(presel, (self.exc_select_statement), re.IGNORECASE))}'
