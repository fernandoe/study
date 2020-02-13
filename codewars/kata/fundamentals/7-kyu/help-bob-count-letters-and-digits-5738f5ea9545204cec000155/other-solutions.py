# -------------------------------------------------------------------------------------------------

def count_letters_and_digits(s):
    return isinstance(s, str) and sum(map(str.isalnum, s))

# -------------------------------------------------------------------------------------------------

def count_letters_and_digits(s):
    return sum(map(str.isalnum, s))

# -------------------------------------------------------------------------------------------------

import re
def count_letters_and_digits(s):
    if s == None or s == []:
        return 0
    return len(re.findall("[A-Za-z0-9]",s))

# -------------------------------------------------------------------------------------------------

import re
def count_letters_and_digits(s):
    try:
        list = re.findall('[A-Za-z0-9]',s)
        return (len(list))
    except:
        return 0

# -------------------------------------------------------------------------------------------------

def count_letters_and_digits(s):
    count = 0
    for x in s:
        if x.isalpha() or x.isnumeric():
            count += 1
    return count

# -------------------------------------------------------------------------------------------------
