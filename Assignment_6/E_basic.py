from math import inf

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
    if ((n == 2)&(e>1)|((n == 5)&(e>2))|((n == 6)&(e>3))|((n == 12)&(e>7))):
        return 1
    else:
        courses=[minCoursesWithEnergyBudget_rec(j,e-1,n-1,last_course),minCoursesWithEnergyBudget_rec(j,e-2,n-4,last_course),minCoursesWithEnergyBudget_rec(j,e-3,n-5,last_course),minCoursesWithEnergyBudget_rec(j,e-7,n-11,last_course)]
        least=1+min(courses)
        #print("n=",n,"e=",e,"least=",least)
    return least

## Test Code: Do not edit
print(minCoursesWithEnergyBudget(1, 16, 30)) # must be 7
