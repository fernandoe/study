import codewars_test as Test
from code import Potion

# Sample Tests
potions = [
    Potion((153, 210, 199), 32),
    Potion((135,  34,   0), 17),
    Potion((18,   19,  20), 25),
    Potion((174, 211,  13),  4),
    Potion((255,  23, 148), 19),
    Potion((51,  102,  51),  6)
]
a = potions[0].mix(potions[1])
b = potions[0].mix(potions[2]).mix(potions[4])
c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])
d = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[4]).mix(potions[5])
e = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[3]).mix(potions[4]).mix(potions[5])

Test.assert_equals(a.color, (147, 149, 130))
Test.assert_equals(a.volume, 49)
Test.assert_equals(b.color, (135, 101, 128))
Test.assert_equals(b.volume, 76)
Test.assert_equals(c.color, (74, 50, 18))
Test.assert_equals(c.volume, 52)
Test.assert_equals(d.color, (130, 91, 102))
Test.assert_equals(d.volume, 99)
Test.assert_equals(e.color, (132, 96, 99))
Test.assert_equals(e.volume, 103)

# Test Cases
@Test.describe("Fixed tests")
def fixed_tests():
    @Test.it("Tests")
    def it_1():
        potions = [
            Potion((153, 210, 199), 32),
            Potion((135,  34,   0), 17),
            Potion((18,   19,  20), 25),
            Potion((174, 211,  13),  4),
            Potion((255,  23, 148), 19),
            Potion((51,  102,  51),  6)
        ]
        a = potions[0].mix(potions[1])
        b = potions[0].mix(potions[2]).mix(potions[4])
        c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])
        d = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[4]).mix(potions[5])
        e = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[3]).mix(potions[4]).mix(potions[5])
        
        Test.assert_equals(a.color, (147, 149, 130))
        Test.assert_equals(a.volume, 49)
        Test.assert_equals(b.color, (135, 101, 128))
        Test.assert_equals(b.volume, 76)
        Test.assert_equals(c.color, (74, 50, 18))
        Test.assert_equals(c.volume, 52)
        Test.assert_equals(d.color, (130, 91, 102))
        Test.assert_equals(d.volume, 99)
        Test.assert_equals(e.color, (132, 96, 99))
        Test.assert_equals(e.volume, 103)

@Test.describe("Random tests")
def fixed_tests():
    from random import randint as R
    from math import ceil

    class Solution:
        def __init__(self, a, n):
            self.color = a
            self.volume = n
        
        def mix(self, other):
            n = self.volume + other.volume
            a = tuple(ceil((x * self.volume + y * other.volume) / n) for x, y in zip(self.color, other.color))
            return Potion(a, n)

    @Test.it("Tests")
    def it_1():
        for _ in range(100):
            a, n = (R(0, 255), R(0, 255), R(0, 255)), R(1, 20)
            result, user = Solution(a, n), Potion(a, n)
            for _ in range(R(1, 5)):
                a, n = (R(0, 255), R(0, 255), R(0, 255)), R(1, 20)
                result, user = result.mix(Solution(a, n)), user.mix(Potion(a, n))
                Test.assert_equals(user.color, result.color)
                Test.assert_equals(user.volume, result.volume)
