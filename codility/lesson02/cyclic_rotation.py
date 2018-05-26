def shift_array(array):
    if not array:
        return array
    last = array.pop()
    array.insert(0, last)
    return array


def cyclic_rotation(A, K):
    result = A
    for i in range(K):
        result = shift_array(result)
    return result
