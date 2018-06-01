from unittest import TestCase
from .solution import solution


class TestSolution(TestCase):

    def test_solution1(self):
        test_case = [1, 3, 6, 4, 1, 2]
        expected = 5
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)

    def test_solution2(self):
        test_case = [1, 2, 3]
        expected = 4
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)

    def test_solution3(self):
        test_case = [-1, -3]
        expected = 1
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)
