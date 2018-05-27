def solution(A):
    summary = {}
    for number in A:
        if number in summary:
            summary[number] += 1
        else:
            summary[number] = 1

    for k, v in summary.items():
        if v == 1:
            return k
