# https://leetcode.com/problems/palindrome-number/submissions/

# My solution - First round
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        x2 = x1[::-1]
        return x1 == x2


tests = [
    (
        (121, ),
        True
    ),
    (
        (-121, ),
        False
    ),
    (
        (10, ),
        False
    ),
]
