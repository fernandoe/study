# Solution 2
def solution(A):
    permutation = sorted(A)
    for idx, value in enumerate(permutation):
        if idx + 1 != value:
            return 0
    return 1

# # Solution 1
# def solution(A):
#     permutation = sorted(A)
#     for i in range(1, permutation[-1] + 1):
#         if i != permutation[i-1]:
#             return 0
#     return 1
