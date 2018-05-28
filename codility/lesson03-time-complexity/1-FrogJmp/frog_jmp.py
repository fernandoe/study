# X: frog position
# Y: final position
# D: jump distance


# Round 3
def solution(X, Y, D):
    distance = Y - X
    return 0 if distance == 0 else int(distance / D) + 1


# Round 2
# def solution(X, Y, D):
#     count = 0
#     while X < Y:
#         count += 1
#         X += D
#     return count

# Round 1
# def solution(X, Y, D):
#     count = 0
#     while X <= Y:
#         count += 1
#         X += D
#     return count
