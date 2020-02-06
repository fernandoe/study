# -------------------------------------------------------------------------------------------------

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")

# -------------------------------------------------------------------------------------------------

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

# -------------------------------------------------------------------------------------------------

import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

# -------------------------------------------------------------------------------------------------