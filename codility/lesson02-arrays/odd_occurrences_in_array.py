def solution(A):
    summary = []
    for number in A:
        if number in summary:
            summary.remove(number)
        else:
            summary.append(number)
    return summary[0]

# def solution(A):
#     result = 0
#     for number in A:
#         result ^= number
#     return result
