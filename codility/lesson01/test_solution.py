from unittest import TestCase

from codility.lesson01.solution import solution


class TestSolution(TestCase):

    def test_solution_1041(self):
        result = solution(1041)
        self.assertEqual(5, result)

    def test_solution_32(self):
        result = solution(32)
        self.assertEqual(0, result)

    def test_solution_9(self):
        result = solution(9)
        self.assertEqual(2, result)

    def test_solution_529(self):
        result = solution(529)
        self.assertEqual(4, result)

    def test_solution_20(self):
        result = solution(20)
        self.assertEqual(1, result)

    def test_solution_15(self):
        result = solution(15)
        self.assertEqual(0, result)

    def test_multiples_n(self):
        for i in range(1, 50):
            solution(i)
