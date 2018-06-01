# Solution 1
def solution(A):
    bigger = max(A)
    if bigger <= 0:
        return 1

    for i in range(1, bigger):
        if i not in A:
            return i

    return bigger + 1
