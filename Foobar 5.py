

def generateAllBinaryStrings(n):
    pattern = [-1]*n
    allCombs = []
 
    # create an empty stack (we can also use set, list, or any other container)
    stack = deque()
    stack.append(pattern) # push the pattern into the stack
 
    # loop till stack is empty
    while stack:
 
        # pop a string from the stack and process it
        curr = stack.pop()
 
        # `index` stores position of the first occurrence of wildcard
        # pattern in `curr`
        index = curr.find(-1)
        if index != -1:
            # replace `?` with 0 and 1 and push it into the stack
            curr[index]=0
            stack.append(curr)
            curr[index]=1
            stack.append(curr)
 
        # if no wildcard pattern is found, print the string
        else:
            allCombs.append(curr)
    return allCombs

'''
def generateAllBinaryStrings(n, arr, i): 
    if i == n:
        allBinary.append(arr.copy())
        return
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1) 
  
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1) 
'''
def copy(arr):
    arr2 = []
    for i in arr:
        arr2.append(i)
    return arr2

def deepCopy2d(arr):
    newArr = []
    for arr2 in arr:
        newArr.append(copy(arr))
    return newArr

def doRowsWork(g, i, prevRow, curRow):
    #Check if rows give correct values
    giveCorrect = True
    for j in range(len(g)):
        thisSum = prevRow[j]+prevRow[j+1]+curRow[j]+curRow[j+1]
        if ((thisSum == 1 and g[j][i] == False) or ((not thisSum == 1) and g[j][i] == True)):
            giveCorrect = False
            j = len(g)
    return giveCorrect



def solution(g):
    height = len(g)+1
    width = len(g[0])+1

    allBinary = generateAllBinaryStrings(height)

    possibilities = deepCopy2d(allBinary)

    allFirstCols = []
    
    for pos in possibilities:
        works = True
        for y in range(height-1):
            if (g[y][0] == 1 and pos[y] == 1 and pos[y+1] == 1):
                works = False
        if (works):
            allFirstCols.append(copy(pos))


    #For each additional col, make a 2d array holding
    #every possible column for that col and put the num of possibilities so far
    #with that col in a parallel 2d array
    
    allPossibilities = []
    allPossibilities.append(allFirstCols)

    parallelVals = []
    parallelVals.append([1]*len(allFirstCols))

    #Iterate through remaining cols

    for i in range(1, width):
        #Append empty "dictionary" entries
        allPossibilities.append(allBinary)
        parallelVals.append([0]*len(allBinary))
        #Loop through every possible previous row and check every new row
        for j in range(len(parallelVals[i-1])):
            for k in range(len(parallelVals[i])):
                prevRow = allPossibilities[i-1][j]
                currentRow = allPossibilities[i][k]
                result = doRowsWork(g, i-1, prevRow, currentRow)
                #If result is true, add prevRow dict val to currentRow dict val
                #print(result)
                if (result):
                    parallelVals[i][k]+=parallelVals[i-1][j]
    total = sum(parallelVals[width-1])
    return total


