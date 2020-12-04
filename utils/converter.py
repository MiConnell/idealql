import re
from typing import List

import pandas as pd

import file_preprocessing
import fql
from utils import parser

df = pd.DataFrame()

# This is just here so no errors are raised
def execute(query: str) -> List[str]:
    query = query
    return ["COLUMN3", "COLUMN4"]


# carry on


conn = file_preprocessing.conn


class ConvertSelect:
    """
    EXCLUDING COLUMN4 SELECT * FROM _TABLE_
    ->
    SELECT COLUMN1, COLUMN2, COLUMN3, COLUMN5 FROM _TABLE_
    """

    def __init__(self, excluded_columns: List[str]) -> None:
        self.excluded_columns = excluded_columns
        self.other_columns = (
            self._included_columns(self.excluded_columns)
            if self.excluded_columns is not None
            else None
        )

    # get all columns except excluded from database
    def _included_columns(self, excluded_columns: List[str]) -> None:
        self.lex = parser.Lexer(fql.FILE_NAME)
        self.excluded_columns = excluded_columns
        self.inclusive_select_statement = f"""
                SELECT COLUMN_NAME FROM
                INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = {self.lex.from_table}
                AND COLUMN_NAME NOT IN
                ({", ".join(self.excluded_columns)})
        """
        self.included_columns = execute(
            self.inclusive_select_statement
        )  # need to actually run the query

    # take columns from _included_columns and replace * in SELECT with those columns
    def inclusive_select(self) -> str:
        self.exc_select_statement: str = self.lex.file_text.replace(
            "*", ", ".join(iter(self.included_columns))
        )
        presel = "(?<=select).*"
        return f'SELECT{"".join(re.findall(presel, (self.exc_select_statement), re.IGNORECASE))}'
