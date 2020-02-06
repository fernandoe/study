VOWELS = "aeiouAEIOU"


def remove_vowels(string):
    return [letter for letter in string if letter not in VOWELS]
    

def disemvowel(string):
    return ''.join(remove_vowels(string))


if __name__== "__main__":
    print(disemvowel("This website is for losers LOL!"))

# tests = [("This website is for losers LOL!", "Ths wbst s fr lsrs LL!"),
#          ("No offense but,\nYour writing is among the worst I've ever read", "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"),
#          ("What are you, a communist?", "Wht r y,  cmmnst?")]

# for case in tests:
#     test.assert_equals(disemvowel(case[0]), case[1])