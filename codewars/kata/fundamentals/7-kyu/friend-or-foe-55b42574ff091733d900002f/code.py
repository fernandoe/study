def filter_friends(friend):
    return len(friend) == 4


def friend(x):
    return list(filter(filter_friends, x))


if __name__== "__main__":
    import codewars_test as test

    # Sample Tests
    test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
    test.assert_equals(friend(['']), [])
    test.assert_equals(friend(['Ryan']), ['Ryan'])

    # Test Cases
    test.describe("Fixed Tests")

    test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
    test.assert_equals(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
    test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])
    test.assert_equals(friend(["Love", "Your", "Face", "1"]), ["Love", "Your", "Face"])
    test.assert_equals(friend(["Hell", "Is", "a", "badd", "word"]), ["Hell", "badd", "word"])
    test.assert_equals(friend(["Issa", "Issac", "Issacs", "ISISS"]), ["Issa"])
    test.assert_equals(friend(["Robot", "Your", "MOMOMOMO"]), ["Your"])
    test.assert_equals(friend(["Your", "BUTT"]), ["Your", "BUTT"])
    test.assert_equals(friend(["Hello", "I", "AM", "Sanjay", "Gupt"]), ["Gupt"])
    test.assert_equals(friend(["This", "IS", "enough", "TEst", "CaSe"]), ["This", "TEst", "CaSe"])
    test.assert_equals(friend([]), [])

    test.describe("Random Tests")

    from random import choice, randint

    def random_tests():
        from string import ascii_letters as l, digits as d
        abc = l + d
        def random_string(friend=False):
            return "".join(choice(abc) for _ in range(friend and 4 or randint(0, 20)))
        
        def random_input():
            return [random_string(randint(0, 100) % 4 == 0) for _ in range(randint(0, 20))]

        def solution(l):
            return [w for w in l if len(w) == 4]

        for _ in range(100):
            ri = random_input()
            test.assert_equals(friend(ri), solution(ri))

    random_tests()
