# https://leetcode.com/problems/two-sum/submissions/1061924644/
from typing import List

# My solution - First round
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a, num1 in enumerate(nums):
            for b, num2 in enumerate(nums):
                if a == b: continue
                if num1 + num2 == target:
                    return [a, b]
        return []


tests = [
    (
        ([2, 7, 11, 15], 9),
        [0, 1]
    ),(
        ([3, 2, 4], 6),
        [1, 2]
    ),(
        ([3, 3], 6),
        [0, 1]
    )
]
