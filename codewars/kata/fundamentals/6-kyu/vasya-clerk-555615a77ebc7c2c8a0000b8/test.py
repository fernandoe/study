import codewars_test as test
from code import tickets

# Sample Tests
# test.assert_equals(tickets([25, 25, 50]), "YES")
# test.assert_equals(tickets([25, 100]), "NO")

# Test Cases
test.assert_equals(tickets([25, 25, 50, 100]), "YES")
# test.assert_equals(tickets([25, 25, 25, 25, 50, 100, 50]), "YES")
# test.assert_equals(tickets([25, 25, 25, 100]), "YES")
# test.assert_equals(tickets([25, 50, 25, 100]), "YES")
# test.assert_equals(tickets([25, 25, 25, 25, 25, 100, 100]), "YES")