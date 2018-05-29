# Solution 1
def solution(A):
    length = len(A)
    minimal = None
    for i in range(1, length):
        distance = abs(sum(A[0:i]) - sum(A[i-length:length]))
        if minimal is None or distance < minimal:
            minimal = distance
    return minimal
