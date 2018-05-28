# X: frog position
# Y: final position
# D: jump distance


def solution(X, Y, D):
    count = 0
    while X <= Y:
        count += 1
        X += D
    return count
