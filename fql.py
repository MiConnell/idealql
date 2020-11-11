import parser

TEST_TEXT = """EXCLUDING (COLUMN2) SELECT
 *, 10 * 10,
FROM TEST_TABLE
WHERE 1 = 1"""

lex = parser.Lexer("fql.py", TEST_TEXT)
