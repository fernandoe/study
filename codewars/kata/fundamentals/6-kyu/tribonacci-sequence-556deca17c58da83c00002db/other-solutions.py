# -------------------------------------------------------------------------------------------------

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res

# -------------------------------------------------------------------------------------------------
def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]

# -------------------------------------------------------------------------------------------------

def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]

# -------------------------------------------------------------------------------------------------

def tribonacci(signature, n):
    output = signature[:n]
    while len(output) < n:
        output.append(sum(output[-3:]))
    return output

# -------------------------------------------------------------------------------------------------

def tribonacci(signature,n):
    result = []
    if n > 3:
        result = signature
        for i in range(0,n-3):
            nextTrib = result[0+i] + result[1+i] + result[2+i]
            print(nextTrib)
            result.append(nextTrib)
    elif n == 3:
        result = signature
    elif n == 2:
        result = [signature[0],signature[1]]
    elif n == 1:
        result = [signature[0]]
    return result

# -------------------------------------------------------------------------------------------------
