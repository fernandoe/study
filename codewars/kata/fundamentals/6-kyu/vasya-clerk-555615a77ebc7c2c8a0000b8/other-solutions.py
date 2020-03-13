# -------------------------------------------------------------------------------------------------

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# -------------------------------------------------------------------------------------------------

def alphabet_position(s):
    return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())

# -------------------------------------------------------------------------------------------------

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')

# -------------------------------------------------------------------------------------------------

from string import ascii_lowercase

def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())

# -------------------------------------------------------------------------------------------------

import string

def alphabet_position(text):
    return " ".join([str(string.lowercase.index(letter.lower())+1) for letter in list(text) if letter.isalpha()])

# -------------------------------------------------------------------------------------------------

def get_positions(text):
    for char in text:
        pos = ord(char)
        if pos >= 65 and pos <= 90:
            yield pos - 64
        if pos >= 97 and pos <= 122:
            yield pos - 96

def alphabet_position(text):
    return " ".join((str(char) for char in get_positions(text)))

# -------------------------------------------------------------------------------------------------
