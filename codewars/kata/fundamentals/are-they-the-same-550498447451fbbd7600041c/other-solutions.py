# -------------------------------------------------------------------------------------------------

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

# -------------------------------------------------------------------------------------------------

def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

# -------------------------------------------------------------------------------------------------

def comp(array1, array2):
    if array1 and array2:
        return sorted([x*x for x in array1]) == sorted(array2)
    return array1 == array2 == []

# -------------------------------------------------------------------------------------------------

def comp(a1, a2):
    return None not in (a1, a2) and all(x**2 == y for x, y in zip(sorted(a1), sorted(a2)))

# -------------------------------------------------------------------------------------------------
