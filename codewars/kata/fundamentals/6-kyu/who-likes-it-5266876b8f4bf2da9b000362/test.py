import codewars_test as Test
from code import likes

# Sample Tests
Test.assert_equals(likes([]), 'no one likes this')
Test.assert_equals(likes(['Peter']), 'Peter likes this')
Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

# Test Cases
Test.describe("Random tests")
from random import randint, shuffle
sol=lambda n: 'no one likes this' if len(n)==0 else n[0]+' likes this' if len(n)==1 else n[0]+' and '+n[1]+' like this' if len(n)==2 else n[0]+', '+n[1]+' and '+n[2]+' like this' if len(n)==3 else n[0]+', '+n[1]+' and '+str(len(n)-2)+' others like this'
base=["Sylia Stingray", "Priscilla S. Asagiri", "Linna Yamazaki", "Nene Romanova", "Nigel", "Macky Stingray", "Largo", "Brian J. Mason", "Sylvie", "Anri", "Leon McNichol", "Daley Wong", "Galatea", "Quincy Rosenkreutz"]

for _ in range(40):
    shuffle(base)
    names=base[:randint(0,len(base)-1)]
    Test.it("Testing for %s" % (", ".join(names) if len(names)>0 else "none"))
    Test.assert_equals(likes(names[:]),sol(names),"It should work for random inputs too")
