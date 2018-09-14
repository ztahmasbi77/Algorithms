from random import getrandbits
def makeOneThirdCoin():     
    n=8
    toss=[]
    condition = False
    for i in range(0,n):
        toss.append(getrandbits(1))
    for i in range(0,n,2):
        if toss[i] == 1:
            sum = 0
            for k in range(i+1,n):
                sum = sum + toss[k]
            if sum == 0:
                condition = True
    return condition

# Test that probability of makeOneThirdCoin() is correct
count = 0
t = 0
nTrials = 10000000
for i in range(nTrials): 
    b = makeOneThirdCoin()
    if (b):
        count = count + 1
print('Count = ', count, ' probability est = ', count/nTrials)
