# X: frog position
# Y: final position
# D: jump distance


# Round 2
def solution(X, Y, D):
    count = 0
    while X < Y:
        count += 1
        X += D
    return count

# Round 1
# def solution(X, Y, D):
#     count = 0
#     while X <= Y:
#         count += 1
#         X += D
#     return count
