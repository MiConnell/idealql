import parser

test_text = """EXCLUDING (COLUMN2) SELECT
 *, 10 * 10,
FROM TEST_TABLE
WHERE 1.24 = 1.67"""

test_text = " ".join(test_text.lower().split()).replace(',', '')

print(test_text)

lex = parser.Lexer("fql.py", test_text)
