from math import inf
data_3B=[]

def minCoursesWithEnergyBudget(j, e, n):
    last_course=False
    if (n % 7 == 2):
        last_course=True
    return minCoursesWithEnergyBudget_rec(j, e, n, last_course)

def minCoursesWithEnergyBudget_rec(j, e, n, last_course):
    if (n % 7 == 2)&(not last_course):
        return inf
    last_course=False
    if e<1:
        return inf
    if n == 1:
        return 0
    if n < 1:
        return inf
    if (((n == 2)&(e>1))|((n == 5)&(e>2))|((n == 6)&(e>3))|((n == 12)&(e>7))):
        return 1
    else:
        courses=[minCoursesWithEnergyBudget_rec(j,e-1,n-1,last_course),minCoursesWithEnergyBudget_rec(j,e-2,n-4,last_course),minCoursesWithEnergyBudget_rec(j,e-3,n-5,last_course),minCoursesWithEnergyBudget_rec(j,e-7,n-11,last_course)]
        least=1+min(courses)
    return least

def minCoursesWithEnergyBudget_Memoize(E, n): # j is assumed to be 1 
    prev_len_n=len(data_3B)
    if prev_len_n<n+1:
        for i in range(n-prev_len_n+1):
            data_3B.append([])
            for j in range(E+1):
                data_3B[prev_len_n+i].append(inf)
    for i in range(prev_len_n):
        prev_len_e=len(data_3B[i])
        if prev_len_e<E+1:
            for j in range(E-prev_len_e+1):
                data_3B[i].append(inf)
    
    last_course=False
    if (n % 7 == 2):
        last_course=True
    return minCoursesWithEnergyBudget_Memoize_rec(E,n,last_course)

from math import inf
def minCoursesWithEnergyBudget_Memoize_rec(E,n,last_course): # Assume that j = 1 is always the starting point.
    if (n % 7 == 2)&(not last_course):
        return inf
    last_course=False
    if n <= 1:
        return inf
    elif E<=0:
        return inf  
    try:
        temp=data_3B[n][E]
    except:
        print("n=",n,"e=",E)
    if temp != inf:
        return temp
    elif (((n == 2)&(E>1))|((n == 5)&(E>2))|((n == 6)&(E>3))|((n == 12)&(E>7))):
        return 1
    else:
        courses=[minCoursesWithEnergyBudget_Memoize_rec(E-1,n-1,last_course),minCoursesWithEnergyBudget_Memoize_rec(E-2,n-4,last_course),minCoursesWithEnergyBudget_Memoize_rec(E-3,n-5,last_course),minCoursesWithEnergyBudget_Memoize_rec(E-7,n-11,last_course)]
        least=1+min(courses)
        if least != inf:
            data_3B[n][E]=least
            least_2=minCoursesWithEnergyBudget(1, E, n)
            if(least!=least_2):
                print("n=",n,"E=",E,"least=",data_3B[n][E])
                print("error-least_2=",least_2)
    return least

## Test Code: Do not edit
print(minCoursesWithEnergyBudget_Memoize(25, 30)) # must be 5
