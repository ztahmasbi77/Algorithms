def findMinimum(a):
    minSoFar=math.inf
    for i in range(len(a)):
        if a[i] < minSoFar:
            minSoFar = a[i]
    return minSoFar

