from unittest import TestCase
from .solution import solution


class TestSolution(TestCase):

    def test_solution1(self):
        test_case = [2, 3, 1, 5]
        expected = 4
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)

    def test_solution2(self):
        test_case = [1]
        expected = 2
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)

    def test_solution3(self):
        test_case = [2]
        expected = 1
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)

    def test_solution4(self):
        test_case = [2, 3, 4]
        expected = 1
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)

    def test_solution5(self):
        test_case = [2, 3, 1]
        expected = 4
        result = solution(test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)
