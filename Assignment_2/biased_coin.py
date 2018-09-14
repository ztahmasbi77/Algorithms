import random
from datetime import datetime
random.seed(datetime.now())
def flip_coin():
    return random.randint(0,1)
n=20
True_count=0
False_count=0
Total_count=100000
for j in range(0,Total_count):
    toss=[]
    condition = False
    for i in range(0,n):
        toss.append(flip_coin())
    for i in range(0,n,2):
        if toss[i] == 1:
            sum = 0
            for k in range(i+1,n):
                sum = sum + toss[k]
            if sum == 0:
                condition = True
    if condition:
        True_count = True_count + 1
    else:
        False_count = False_count + 1
print("True cases = ",True_count)
print("False cases = ", False_count)
print("Total cases = ", Total_count)
print("True Probability = ", True_count/Total_count)
