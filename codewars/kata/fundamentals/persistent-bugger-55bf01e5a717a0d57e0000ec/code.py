from operator import mul
import functools


def calculate(n, multiplicative):
    if len(str(n)) == 1: return n, multiplicative
    numbers = [int(i) for i in str(n)]
    result = functools.reduce(mul, numbers)
    return calculate(result, multiplicative+1)


def persistence(n):
    if len(str(n)) == 1: return 0
    n, m = calculate(n, 0)
    return m



if __name__== "__main__":
    import codewars_test as test

    # Sample Tests
    test.it("Basic tests")
    test.assert_equals(persistence(39), 3) # 3*9=27 - 2*7=14 - 1*4=4
    test.assert_equals(persistence(4), 0)
    test.assert_equals(persistence(25), 2)
    test.assert_equals(persistence(999), 4)

    # Test Case
    from functools import reduce
    from random import randint
    #-----------------
    def soluce(n):
            digits = [int(d) for d in str(n)]
            if (len(digits) == 1):
                return 0
            p = reduce(lambda x, y : x * y, digits, 1)
            return 1 + soluce(p)
    #-----------------
    test.it("Basic tests")
    test.assert_equals(persistence(39), 3)
    test.assert_equals(persistence(4), 0)
    test.assert_equals(persistence(25), 2)
    test.assert_equals(persistence(999), 4)
    test.assert_equals(persistence(444), 3)

    test.describe("Random tests")
    for _ in range(50):
        n = randint(1, 500000)
        test.it("Testing for: " + str(n))  
        test.assert_equals(persistence(n), soluce(n))
