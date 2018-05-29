from unittest import TestCase
from .solution import solution


class TestSolution(TestCase):

    def test_solution1(self):
        test_case = [3, 1, 2, 4, 3]
        expected = 1
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)

    def test_solution2(self):
        test_case = [3, 3]
        expected = 0
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)

    def test_solution3(self):
        test_case = [1000, -1000]
        expected = 2000
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)
