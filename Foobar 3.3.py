def printMatrix(m):
    for i in range(0, len(m)):
        print(m[i])
    print("\n")


def convertInputToReq(data):
    matrix1 = data
    width = len(data)
    terminalStates = []
    for i in range(0, width):
        #are all in the row 0?
        all0 = True
        rowSum = sum(data[i])
        if (rowSum==0):
            terminalStates.append(i)
        else:
            for j in range(0, width):
                if (data[i][j] != 0):
                    matrix1[i][j] = [data[i][j], rowSum]
                    
    #Move each terminal state row to the beginning
    matrix2 = []
    for i in terminalStates:
        matrix2.append(matrix1[i])
    for i in range(0, width):
        if not i in terminalStates:
            matrix2.append(matrix1[i])

    #Move each terminal state column to the beginning
    matrix3 = []
    for i in range(0, width):
        matrix3.append([])
        for j in terminalStates:
            matrix3[i].append(matrix2[i][j])
        for j in range(0, width):
            if not j in terminalStates:
                matrix3[i].append(matrix2[i][j])

    #Add identity elements to the first len(terminalStates) elements
    for i in range(len(terminalStates)):
        matrix3[i][i] = [1, 1]

    return matrix3, len(terminalStates)
    

def identityMatrix(x):
    identity = []
    for i in range(0, x):
        identity.append([])
        for j in range(0, x):
            if (i == j):
                identity[i].append([1,1])
            else:
                identity[i].append(0)
    return identity

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify(c):
    if (c != 0):
        gcdVal = gcd(c[0],c[1])
        return [int(c[0]/gcdVal), int(c[1]/gcdVal)]
    else:
        return 0

def commonDenomAdd(a, b):
    if (a==0):
        return b
    elif (b==0):
        return a
    else:
        raw = [a[0]*b[1]+a[1]*b[0], a[1]*b[1]]
        return simplify(raw)
    
def simplifyMultiply(a, b):
    if (a==0 or b == 0):
        return 0
    else:
        raw = [a[0]*b[0], a[1]*b[1]]
        return simplify(raw)

def simplifyDivide(a, b):
    #if a is 0, return 0
    #if b is 0, print error
    #otherwise, raw=[a[0]*b[1], a[1]*b[0]]
    if (a == 0):
        return 0
    elif (b == 0):
        print("ERROR")
    else:
        raw=[a[0]*b[1], a[1]*b[0]] 
        return simplify(raw)

def matrixSubtract(a, b):
    returnMat = []
    for i in range(len(a)):
        returnMat.append([])
        for j in range(len(a)):
            bNegated = b[i][j]
            if (not bNegated == 0):
                bNegated[0] = (-1)*b[i][j][0]
            returnMat[i].append(commonDenomAdd(a[i][j], bNegated))
    return returnMat

def matrixMinor(a, m, n):
    #remove row m and column n
    subMatrix = []
    for i in range(len(a)):
        subMatrix.append([])
        for j in range(len(a)):
            subMatrix[i].append(a[i][j])
    subMatrix.pop(m)
    for j in range(0, len(subMatrix)):
        subMatrix[j].pop(n)
    return subMatrix

def matrixDeterminant(a):
    if (len(a) == 1):
        return a[0][0]
    else:
        determinant = 0
        for i in range(len(a)):
            #Add contribution to determinant from top row of matrix a
            cofactorMultiplier = (-1)**(i)
            minorMat = matrixMinor(a, 0, i)
            minorDet = matrixDeterminant(minorMat)
            minorDet = simplifyMultiply(minorDet, a[0][i])
            if (minorDet != 0):
                minorDet[0]*=cofactorMultiplier
                determinant = commonDenomAdd(determinant, minorDet)
        return determinant

def matrixTranspose(a):
    transpose = []
    for i in range(len(a)):
        transpose.append([])
        for j in range(len(a)):
            transpose[i].append(a[j][i])
    return transpose

    
def matrixInverse(a):
    #Find cofactor matrix of a
    cofactors = []
    for i in range(0, len(a)):
        cofactors.append([])
        for j in range(0, len(a)):
            #Create submatrix without row i or column j
            subMatrix = matrixMinor(a, i, j)
            #Find determinant of subMatrix
            determinant = matrixDeterminant(subMatrix)
            #Append
            if (determinant != 0):
                determinant[0]*=((-1)**(i+j))
            cofactors[i].append(determinant)
    cofactorTranspose = matrixTranspose(cofactors)
    aDeterminant = matrixDeterminant(a)
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            cofactorTranspose[i][j] = simplifyDivide(cofactorTranspose[i][j], aDeterminant)
    return cofactorTranspose

def matrixProduct(a, b):
    product = []
    for i in range(len(a)):
        product.append([])
        for j in range(len(b[0])):
            ijEntry = 0
            for k in range(len(b)):
                ijEntry = commonDenomAdd(ijEntry, simplifyMultiply(a[i][k],b[k][j]))
            product[i].append(ijEntry)
    return product

def getFirstNonzeroElement(a):
    for i in range(len(a)):
        if (a[i] != 0):
            return a[i][1]
    return 0
            
def scrapeTopRow(a):
    if (len(a)==0):
        return [1,1]
    
    returnVals = []
    smallestLCM = 1
    for i in range(len(a[0])):
        if (a[0][i] != 0):
            smallestLCM = smallestLCM*a[0][i][1]//gcd(smallestLCM, a[0][i][1])
    for i in range(len(a[0])):
        if (a[0][i] != 0):
            returnVals.append(int(a[0][i][0]*smallestLCM/a[0][i][1]))
        else:
            returnVals.append(0)
    returnVals.append(sum(returnVals))
    return returnVals

def findR(data, numTerminal):
    R = []
    for i in range(numTerminal, len(data)):
        R.append([])
        for j in range(0, numTerminal):
            R[i-numTerminal].append(data[i][j])
    return R

def findQ(data, numTerminal):
    Q = []
    for i in range(numTerminal, len(data)):
        Q.append([])
        for j in range(numTerminal, len(data)):
            Q[i-numTerminal].append(data[i][j])
    return Q

def solution(m):
    reqInput = convertInputToReq(m)
    reqMatrix = reqInput[0]
    numTerminal = reqInput[1]

    qMatrix = findQ(reqMatrix, numTerminal)
    rMatrix = findR(reqMatrix, numTerminal)
    iminusq = matrixSubtract(identityMatrix(len(reqMatrix)-numTerminal),qMatrix)

    fMatrix = matrixInverse(iminusq)

    frMatrix = matrixProduct(fMatrix, rMatrix)
    topRow = scrapeTopRow(frMatrix)
    return topRow
