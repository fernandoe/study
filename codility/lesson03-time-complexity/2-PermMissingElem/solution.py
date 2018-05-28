# Solution 3
def solution(A):
    total = len(A)
    items_sorted = sorted(A)
    for position in range(1, total+1):
        if items_sorted[position-1] == position:
            continue
        else:
            return position
    return total + 1


# # Solution 2
# def solution(A):
#     if not A:
#         return 1
#     if 1 not in A:
#         return 1
#     size = len(A)
#     for i in range(size):
#         idx = i + 1
#         if idx not in A:
#             return idx


# # Solution 1
# def solution(A):
#     print(f"A: {A}")
#     A.sort()
#     for idx, value in enumerate(A):
#         if value + 1 != A[idx + 1]:
#             return value + 1
