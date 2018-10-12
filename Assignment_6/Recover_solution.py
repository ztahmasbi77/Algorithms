from math import inf
data_2={}

def minCoursesForJane_Solution(n): # Assume that j = 1 is always the starting point
    append_value=0
    if n == 1:
        return [0,[]]
    elif n <= 0:
        return [inf,[]]
    else:
        least=inf
        try:
            d=data_2[n-1]
        except KeyError:   
            d=minCoursesForJane_Solution(n-1)
        try:
            c=data_2[n-4]
        except KeyError:   
            c=minCoursesForJane_Solution(n-4)
        try:
            b=data_2[n-5]
        except KeyError:   
            b=minCoursesForJane_Solution(n-5)
        try:
            a=data_2[n-11]
        except KeyError:   
            a=minCoursesForJane_Solution(n-11)
        compare=[a[0],b[0],c[0],d[0]]
        least=min(compare)
        if a[0]==least:
            append_value=11
            final=a
        elif b[0]==least:
            append_value=5
            final=b
        elif c[0]==least:
            append_value=4
            final=c
        elif d[0]==least:
            append_value=1
            final=d 
        k=[0,[]]
        k[0]=int(final[0])+1
        for x in final[1]:
            k[1].append(x)
        k[1].append(append_value)
        data_2[n]=k
        return data_2[n]

## Test Code: Do not edit
print(minCoursesForJane_Solution(9)) # should be 2, [4, 4]
print(minCoursesForJane_Solution(100))
print(minCoursesForJane_Solution(1000))
print(minCoursesForJane_Solution(1500))
print(minCoursesForJane_Solution(2000))
