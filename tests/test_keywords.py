import fql


TEST_TEXT = """
SELECT TOP 2 * FROM IV00101 WHERE ITEMNMBR = 'SK-1499N-GRY'
"""

lex = fql.Lexer(text=TEST_TEXT)

def test_kw_findings():
    assert lex.keyword_list == ['SELECT', 'TOP', 'FROM', 'WHERE', ]
