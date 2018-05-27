from unittest import TestCase

from codility.lesson02.odd_occurrences_in_array import solution


class TestSolution(TestCase):
    def test_solution1(self):
        result = solution([9, 3, 9, 3, 9, 7, 9])
        self.assertEqual(7, result)
