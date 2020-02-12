def unique_in_order(iterable):
    last_element = None
    result = []
    for element in iterable:
        if last_element is None:
            last_element = element
            result.append(element)
        else:
            if last_element != element:
                last_element = element
                result.append(element)
    return result



if __name__== "__main__":
    import codewars_test as test

    # Sample tests
    test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])

    # Test Cases
    test.describe("lets test it")
    test.it("should work with empty array")
    test.assert_equals(unique_in_order(''),[])
    test.it("should work with one element")
    test.assert_equals(unique_in_order('A'),['A'])
    test.it("should reduce duplicates")
    test.assert_equals(unique_in_order('AA'),['A'])        
    test.assert_equals(unique_in_order('AAAABBBCCDAABBB'),['A', 'B', 'C', 'D', 'A', 'B'])
    test.assert_equals(unique_in_order('AADD'),['A','D'])
    test.assert_equals(unique_in_order('AAD'),['A','D'])
    test.assert_equals(unique_in_order('ADD'),['A','D'])
    test.it("and treat lowercase as different from uppercase")
    test.assert_equals(unique_in_order('ABBCcAD'),['A', 'B', 'C', 'c', 'A', 'D'])
    test.it("and work with int arrays")
    test.assert_equals(unique_in_order([1,2,3,3]),[1,2,3])
    test.it("and work with char arrays")
    test.assert_equals(unique_in_order(['a','b','b']),['a','b'])
