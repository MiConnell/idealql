import re

test_query = """excluding addresses, items, customers SELECT customers,
items FROM TEST_TABLE
where customers is NULL having sum(t) > 1;"""

test_query = " ".join(test_query.lower().split())

excols = "(?<=excluding)(.*)(?=select)"
excluded_ = "".join(re.findall(excols, test_query)).split()

presel = "(?<=select).*"
after_select = f'select{"".join(re.findall(presel, (test_query)))}'

# print(test_query)
print(excluded_)
print(after_select)
