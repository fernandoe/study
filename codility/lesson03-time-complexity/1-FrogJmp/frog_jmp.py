# X: frog position
# Y: final position
# D: jump distance


# Round 5
def solution(X, Y, D):
    distance = Y - X
    jumps = distance / D
    decimal_needs = jumps % 1
    if decimal_needs == 0:
        return int(jumps)
    else:
        return int(jumps) + 1

# Round 4
# def solution(X, Y, D):
#     distance = Y - X
#     jumps = distance / D
#     decimal_needs = jumps % 1
#     if decimal_needs == 0:
#         return jumps
#     else:
#         return int(jumps) + 1

# Round 3
# def solution(X, Y, D):
#     distance = Y - X
#     return 0 if distance == 0 else int(distance / D) + 1

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
