# Solution 1
def solution(X, A):
    path = set()
    for idx, place in enumerate(A):
        path.add(place)
        if len(path) == X:
            return idx
    return -1
