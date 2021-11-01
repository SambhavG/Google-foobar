def solution(n):
    coefficients = [0 for x in range(201)]
    coefficients[0] = 1
    coefficients[1] = 1
    for i in range(2, 201):
        for j in range(200, i-1, -1):
            coefficients[j]+=coefficients[j-i]
    return coefficients[n]-1

