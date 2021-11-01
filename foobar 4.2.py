import copy

def bellmanFord(times, time_limit):

    n = len(times)
    a = [[float('inf')]*n for _ in range(n)]
    for i in range(len(times)): #i is the current vertex
        a[i][i] = 0 #We can travel to i in 0 time minimum
        for _ in range(len(times)-1): #Run the following loop n-1 times
            for u in range(len(times)): 
                for v in range(len(times)): #For each pair of vertices u, v
                    if a[i][v] > a[i][u] + times[u][v]:
                        a[i][v] = a[i][u] + times[u][v]
        for u in range(len(times)):
            for v in range(len(times)):
                if a[i][v] > a[i][u] + times[u][v] and a[0][u] < time_limit:
                    return True, a
    return False, a


def solution(times, time_limit):
    if len(times) <= 2:
        return []

    negativeCycle, optimTimes = bellmanFord(times, time_limit)

    if negativeCycle:
        return [x for x in range(len(times)-2)]
    else:
        stack = [[0,[0],time_limit,[[i] for i in range(len(times))]]] #bfs
        vertices = set([i for i in range(len(times))])
        optimSet = set()
        maxSize = 0
        while stack:
            [u,path,timeLeft, nullVerts] = stack.pop()
            for v in (vertices - set(nullVerts[u])):
                nextNull = copy.deepcopy(nullVerts)
                uv = optimTimes[u][v]
                vb = optimTimes[v][len(times)-1]
                vu = optimTimes[v][u]
                if uv+vu == 0:
                    nextNull[u].append(v)
                    nextNull[v].append(u)
                if timeLeft-uv-vb >= 0:
                    nextPath = path+[v]
                    nextTimeLeft=timeLeft-uv
                    stack.append([v,nextPath,nextTimeLeft,nextNull])
                    if v == len(times)-1: 
                        setNextPath = set(nextPath)
                        lengthNextPath = len(setNextPath)
                        if lengthNextPath == len(times):
                            return [x for x in range(len(times)-2)]
                        if maxSize < lengthNextPath or (maxSize == lengthNextPath and sum(optimSet) > sum(setNextPath)):
                            optimSet = setNextPath
                            maxSize = lengthNextPath
        return sorted([x-1 for x in (optimSet - set([0,len(times)-1]))])
