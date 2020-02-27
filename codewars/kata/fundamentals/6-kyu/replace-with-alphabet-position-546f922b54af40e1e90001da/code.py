# Current Points: 134 -> 142
import string

def alphabet_position(text):
    alphabet = string.ascii_lowercase
    result = []
    for char in text:
        if char.lower() in alphabet:
            result.append(str(alphabet.index(char.lower()) + 1))
    return " ".join(result)
