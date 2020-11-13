import parser
import sys
from typing import List
import re

sys.path.append("../")

import pandas as pd

df = pd.DataFrame()

query_file = "../queries.fql"

lex = parser.Lexer(query_file)

excluding = lex.excluded_columns

print(lex.body, excluding)

# This is just here so no errors are raised
def execute(query: str) -> List[str]:
    query = query
    return ['COLUMN3', 'COLUMN4']
# Carry on

class ConvertSelect:
    def __init__(self, excluded_columns: List[str]) -> None:
        self.excluded_columns = excluded_columns
        if self.excluded_columns is not None:
            self.other_columns = self._included_columns(self.excluded_columns)

    def _included_columns(self, excluded_columns: List[str]) -> str:
        self.inclusive_select_statement = f"""
                SELECT COLUMN_NAME FROM
                INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = {lex.from_table}
                AND COLUMN_NAME NOT IN
                ({", ".join(excluded_columns)})
        """
        self.included_columns = execute(self.inclusive_select_statement)  # need to actually run the query

    def inclusive_select(self) -> str:
        self.exc_select_statement: str = lex.file_text.replace(
            "*", ", ".join(iter(self.included_columns))
        )
        presel = "(?<=select).*"
        return f'SELECT{"".join(re.findall(presel, (self.exc_select_statement), re.IGNORECASE))}'


"""
EXCLUDING COLUMN4 SELECT * FROM _TABLE_

->

SELECT COLUMN1, COLUMN2, COLUMN3, COLUMN5 FROM _TABLE_
"""
