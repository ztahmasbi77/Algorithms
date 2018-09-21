def find_fixed_point(data):
    n = len(data)
    if n == 1:
        if data[0] == 0:
            return 0
        else:
            return -1
    elif n == 2:
        if data[0] == 0:
            return 0
        elif data[1] == 1:
            return 1
        else:
            return -1
    mid = int(len(data)/2)
    if data[mid] == mid:
        return mid
    elif data[mid] < mid:
        temp=data[mid+1:]
        for i in range(0,len(temp)):
            temp[i] -= mid+1
        temp_return = find_fixed_point(temp)
        if temp_return == -1:
            return -1
        return mid + 1 + temp_return
    elif data[mid] > mid:
        return find_fixed_point(data[:mid])
    # END

## TESTING CODE : DO NOT EDIT
from random import sample
def find_fixed_point_very_naive(a):
    n = len(a)
    for i in range(0, n):
        if a[i] == i:
            return i
    return -1

a1 = [-1, 0, 2, 3, 10, 12]
j1 = find_fixed_point(a1)
print('j1=', j1)
assert a1[j1] == j1, 'Failed test a1'

a2 = [-1, 0, 4, 8, 15, 32]
j2 = find_fixed_point(a2)
print('j2 = ', j2)
assert j2 == -1, ' Failed test a2'

a3 = [0, 1, 2, 3, 4, 5, 6, 7, 9]
j3 = find_fixed_point(a3)
print('j3 = ', j3)
assert a3[j3] == j3, ' Failed test a3'


a4 = [0]
j4 = find_fixed_point(a4)
print('j4 = ', j4)
assert a4[j4] == j4, ' Failed test a4'


def test_find_fixed_point_code(n_tests, test_size):
    n_passed = 0
    for i in range(0, n_tests):
        a = sorted(sample( range(-test_size,  test_size ), test_size))
        j = find_fixed_point(a)
        k = find_fixed_point_very_naive(a)
        if (j >= 0 and a[j] != j): 
            print(' Code failed for input: ', a, 'returned : ', j, ' (not a fixed point) expected:', k)
        elif (j == -1 and k != -1):
            print(' Code failed for input: ', a, 'returned : ', j, ' but expected fixed point:', k)
        else:
            n_passed = n_passed + 1
            
    return n_passed

n_tests = 10000
n_passed = test_find_fixed_point_code(n_tests, 20)
print(' num tests  = ', n_tests)
print(' num passed = ', n_passed)

## END TESTS For find_fixed_point
