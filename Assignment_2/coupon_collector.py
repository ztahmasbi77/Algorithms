import random
def simulateCouponCollection(n):
    all_coupons_collected = False
    b=[]
    counter = 0
    for i in range(0,n):
        b.append(0)
    while(not all_coupons_collected):
        counter = counter + 1
        j=random.randint(0,n-1)
        b[j]=1
        all_coupons_collected = True
        for i in range(0,n):
            if b[i]==0:
                all_coupons_collected = False
    return counter
def runCouponCollectionExperiment(nMax):
    returnData = {}
    average=0
    for i in range(10,nMax+10,10):
        for j in range(0,1000):
            average = (average * j + simulateCouponCollection(i))/(j+1)
        returnData[i]=average
    return returnData
def runHistogram(n, numTrials):
    lst = []
    for i in range(numTrials):
        lst.append(simulateCouponCollection(n))
    return lst
lst = runHistogram(500, 5000)
average = 0
for i in range(0,5000):
    average = (average * i + lst[i])/(i+1)
print(average)
