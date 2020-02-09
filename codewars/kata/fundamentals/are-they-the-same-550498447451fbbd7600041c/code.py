def comp(array1, array2):
    if (array1 is None or array2 is None):
        return False

    if (len(array1) != len(array2)):
        return False
    elif len(array1) == 0:
        return True

    for item in array1:
        square = item**2
        if square in array2:
            array2.remove(square)
            continue
        else:
            return False

    return len(array2) == 0
	


if __name__== "__main__":
    import codewars_test as test

    # Sample Tests
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    test.assert_equals(comp(a1, a2), True)
    a = [121, 144, 19, 161, 19, 144, 19, 11]  
    b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
    test.assert_equals(comp(a, b), False)
    a = [121, 144, 19, 161, 19, 144, 19, 11]  
    b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
    test.assert_equals(comp(a, b), False)
    test.assert_equals(comp([], b), False)
    test.assert_equals(comp(a, []), False)
    test.assert_equals(comp([], []), True)
    
    # Test Case
    test.describe("Basic tests")
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    test.assert_equals(comp(a1, a2), True)
    a1 = [4, 4]
    a2 = [1, 31]
    test.assert_equals(comp(a1, a2), False)
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    test.assert_equals(comp(a1, a2), False)
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    test.assert_equals(comp(a1, a2), False)
    a1 = []
    a2 = []
    test.assert_equals(comp(a1, a2), True)
    a1 = []
    a2 = None
    test.assert_equals(comp(a1, a2), False)
    a1 = [121, 144, 19, 161, 19, 144, 19, 11, 1008]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    test.assert_equals(comp(a1, a2), False)
    a1 = [10000000, 100000000]
    a2 = [10000000 * 10000000, 100000000 * 100000000]
    test.assert_equals(comp(a1, a2), True)
    a1 = [10000001, 100000000]
    a2 = [10000000 * 10000000, 100000000 * 100000000]
    test.assert_equals(comp(a1, a2), False)
    a1 = [2, 2, 3]
    a2 = [4, 9, 9]
    test.assert_equals(comp(a1, a2), False)
    a1 = [2, 2, 3]
    a2 = [4, 4, 9]
    test.assert_equals(comp(a1, a2), True)
    a1 = None
    a2 = []
    test.assert_equals(comp(a1, a2), False)
    test.assert_equals(comp([], [1]), False)
    a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    test.assert_equals(comp(a1, a2), True)

    test.describe("Random tests")
    from random import randint

    sol=lambda a1, a2: sorted(a1)==sorted([item**.5 for item in a2]) if a1!=None and a2!=None else False

    for i in range(40):
        a1=[randint(0,100) for i in range(randint(1,8))]
        a2=[elem*elem for elem in a1]
        if randint(0,1)==1: a2[randint(0,len(a2)-1)]+=1
        test.it("Testing for "+str(a1)+" and "+str(a2))
        test.assert_equals(comp(a1[:],a2[:]),sol(a1,a2),"It should work with random inputs too")
