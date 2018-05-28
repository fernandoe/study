from unittest import TestCase
from .frog_jmp import solution


class TestSolution(TestCase):

    def test_solution1(self):
        self.assertEqual(3, solution(10, 85, 30))

    def test_solution2(self):
        self.assertEqual(0, solution(85, 85, 30))

    def test_solution3(self):
        self.assertEqual(2, solution(1, 5, 2))
