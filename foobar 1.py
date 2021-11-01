import math

def solution(i):
    returnChar = ""
    currentPrime = 1;
    while (i > -5):
        currentPrime+=1
        isPrime = True
        for j in range(2, math.floor(currentPrime/2)+1):
            if (currentPrime%j == 0):
                isPrime = False
        if (isPrime):
            for j in str(currentPrime):
                if (i <= 0 and i > -5):
                    returnChar+=j
                i-=1
    print(returnChar)
