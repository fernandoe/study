# Current Points: 126 - 134

def maximum_sum(arr):
    maximum = 0
    for i, item in enumerate(arr):
        partial_max = sum(arr[:i+1])
        if partial_max > maximum:
            maximum = partial_max
    return maximum

def max_sequence(arr):
    maximum = 0
    while len(arr) > 0:
        partial_max = maximum_sum(arr)
        if partial_max > maximum:
            maximum = partial_max
        arr.pop(0)
    return maximum
