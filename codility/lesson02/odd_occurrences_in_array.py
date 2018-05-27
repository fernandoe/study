def solution(A):
    repeated = []
    for value in A:
        counter = A.count(value)
        if counter > 1:
            if value in repeated:
                continue
            else:
                repeated.append(value)
        else:
            return value
