def solution(h, q):
    returnList = []
    for i in q:
        if (i == pow(2, h)-1):
            returnList.append(-1)
        else:
            currentLevel = h
            currentTop = pow(2, h)-1
            currentLower = 1
            currentUpper = pow(2, h)-2
            topList = []
            while currentLevel > 1:
                topList.append(currentTop)
                #prune to left tree
                if (i <= (currentLower+currentUpper-1)/2):
                    currentLevel-=1
                    currentTop = (currentLower+currentUpper-1)/2
                    #currentLower stays the same
                    currentUpper = currentTop-1
                #prune to the right tree
                elif (i > (currentLower+currentUpper-1)/2 and i < currentTop):
                    currentLevel-=1
                    currentTop-=1
                    currentLower = (currentLower+currentUpper-1)/2+1
                    currentUpper = currentTop-1
                if (i == currentTop):
                    returnList.append(int(topList[len(topList)-1]))
                    currentLevel = 0
    return returnList

