MAP = {"A": "T", "T": "A", "C": "G", "G": "C"}


def DNA_strand(dna):
    return "".join([MAP[c] for c in dna])


if __name__ == "__main__":
    import codewars_test as test

    # Sample tests
    test.assert_equals(DNA_strand("AAAA"), "TTTT", "String AAAA is")
    test.assert_equals(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
    test.assert_equals(DNA_strand("GTAT"), "CATA", "String GTAT is")

    # Test Cases
    test.describe("Basic tests")
    test.assert_equals(DNA_strand("AAAA"), "TTTT", "String AAAA is")
    test.assert_equals(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
    test.assert_equals(DNA_strand("GTAT"), "CATA", "String GTAT is")
    test.assert_equals(DNA_strand("AAGG"), "TTCC", "String AAGG is")
    test.assert_equals(DNA_strand("CGCG"), "GCGC", "String CGCG is")
    test.assert_equals(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
    test.assert_equals(
        DNA_strand(
            "GTATCGATCGATCGATCGATTATATTTTCGACGAGATTTAAATATATATATATACGAGAGAATACAGATAGACAGATTA"
        ),
        "CATAGCTAGCTAGCTAGCTAATATAAAAGCTGCTCTAAATTTATATATATATATGCTCTCTTATGTCTATCTGTCTAAT",
    )

    test.describe("Random tests")
    base = ["A", "C", "G", "T"]
    from random import randint

    def DNASol(dna):
        return "".join(
            [
                "A" if nuc == "T" else "T" if nuc == "A" else "C" if nuc == "G" else "G"
                for nuc in dna
            ]
        )

    for _ in range(40):
        testdna = "".join([base[randint(0, 3)] for i in range(randint(5, 30))])
        test.it("testing for " + testdna)
        test.assert_equals(
            DNA_strand(testdna), DNASol(testdna), "It should work for random inputs too"
        )
