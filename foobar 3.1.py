
def solution(x, y):
    x = int(x)
    y = int(y)

    numCycles = 0
    while (x > 1 or y > 1):
        if (x == y or x < 1 or y < 1):
            return "impossible"
        elif (x > y):
            factor = int(x/y)
            numCycles+=factor
            if (y == 1):
                numCycles-=1
                x = x-y*(factor-1)
            else:
                x = x-y*factor
        elif (x < y):
            factor = int(y/x)
            numCycles+=factor
            if (x == 1):
                numCycles-=1
                y = y-x*(factor-1)
            else:
                y = y-x*factor
    return str(numCycles)
