# Current Points: 88

def countOnes(left, right):
    print(f"left: {left} - right: {right}")
    total = 0
    for i in range(left, right + 1):
        total += bin(i).count('1')
    return total
