# -------------------------------------------------------------------------------------------------

def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

# -------------------------------------------------------------------------------------------------

def maxSequence(arr):
  lowest = ans = total = 0
  for i in arr:
    total += i
    lowest = min(lowest, total)
    ans = max(ans, total - lowest)
  return ans

# -------------------------------------------------------------------------------------------------

def maxSequence(arr):
    maxl = 0
    maxg = 0
    for n in arr:
        maxl = max(0, maxl + n)
        maxg = max(maxg, maxl)
    return maxg

# -------------------------------------------------------------------------------------------------

def maxSequence(arr):
    current = 0
    max_found = 0
    
    for value in arr:
        current += value
        if current < 0:
            current = 0
        
        if current > max_found:
            max_found = current
    
    return max_found

# -------------------------------------------------------------------------------------------------

def maxSequence(arr):
    cur_sum, max_sum = 0, 0
    for item in arr:
        cur_sum = max(item, cur_sum+item)
        max_sum = max(max_sum, cur_sum)
    return max_sum

# -------------------------------------------------------------------------------------------------

def maxSequence(arr):
    return max([sum(arr[i:j]) for i in range(len(arr)+1) for j in range(len(arr)+1)])

# -------------------------------------------------------------------------------------------------
