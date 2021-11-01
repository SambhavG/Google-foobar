

def solution(s):
    #create cumulative sum for number of left walkers up to j
    #then for each right walker at i, we add 2*(cumsum[n]-cumsum[i])
    leftCumSum = []

    if (s[0] == '<'):
            leftCumSum.append(1)
    else:
        leftCumSum.append(0)

    
    for i in range(1, len(s)):
        if (s[i] == '<'):
            leftCumSum.append(leftCumSum[i-1]+1)
        else:
            leftCumSum.append(leftCumSum[i-1])
    totalShakes = 0
    for i in range(len(s)):
        if (s[i] == '>'):
            totalShakes+=2*(leftCumSum[len(s)-1]-leftCumSum[i])

    return totalShakes
    
