def count_letters_and_digits(s):
    counter = 0
    for c in s:
        if c.isalpha() or c.isnumeric():
            counter += 1
    return counter


if __name__== "__main__":
    import codewars_test as Test

    # Sample tests
    Test.it('Basic tests')
    Test.assert_equals(count_letters_and_digits('n!!ice!!123'), 7)
    Test.assert_equals(count_letters_and_digits('de?=?=tttes!!t'), 8)
    Test.assert_equals(count_letters_and_digits(''), 0)
    Test.assert_equals(count_letters_and_digits('!@#$%^&`~.'), 0)
    Test.assert_equals(count_letters_and_digits('u_n_d_e_r__S_C_O_R_E'), 10)

    # Test Cases
    from string import ascii_letters, digits, printable
    from random import choices, randint

    def _inner_solution(s):
        return len(list(filter(lambda x: x in ascii_letters + digits, s))) if type(s) is str else 0


    def _random_string(_min=30, _max=100):
        return ''.join(choices(printable, k=randint(_min, _max)))

    Test.it('Basic tests')
    Test.assert_equals(count_letters_and_digits('n!!ice!!123'), 7)
    Test.assert_equals(count_letters_and_digits('de?=?=tttes!!t'), 8)
    Test.assert_equals(count_letters_and_digits(''), 0)
    Test.assert_equals(count_letters_and_digits('!@#$%^&`~.'), 0)
    Test.assert_equals(count_letters_and_digits('u_n_d_e_r__S_C_O_R_E'), 10)

    Test.describe('Random tests')
    for _ in range(50):
        test_string = _random_string()
        Test.it("Testing for: " + test_string)        
        Test.assert_equals(count_letters_and_digits(test_string), _inner_solution(test_string))
