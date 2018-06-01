from unittest import TestCase
from .solution import solution


class TestSolution(TestCase):

    def test_solution1(self):
        test_case = 5, [1, 3, 1, 4, 2, 3, 5, 4]
        expected = 6
        result = solution(*test_case)
        print(f"test_case: {test_case}")
        print(f"expected: {expected}")
        print(f"result: {result}")
        self.assertEqual(expected, result)
