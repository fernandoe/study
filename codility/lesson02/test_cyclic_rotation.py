from unittest import TestCase

from codility.lesson02.cyclic_rotation import cyclic_rotation


class TestCyclicRotation(TestCase):

    def test_cyclic_rotation1(self):
        result = cyclic_rotation([3, 8, 9, 7, 6], 3)
        self.assertEqual([9, 7, 6, 3, 8], result)

    def test_cyclic_rotation2(self):
        result = cyclic_rotation([0, 0, 0], 1)
        self.assertEqual([0, 0, 0], result)

    def test_cyclic_rotation3(self):
        result = cyclic_rotation([1, 2, 3, 4], 4)
        self.assertEqual([1, 2, 3, 4], result)

    def test_cyclic_rotation4(self):
        result = cyclic_rotation([3, 8, 9, 7, 6], 1)
        self.assertEqual([6, 3, 8, 9, 7], result)
