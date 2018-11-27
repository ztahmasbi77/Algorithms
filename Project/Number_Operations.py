def count_of_1(number):
    count = 0
    while number != 0:
        value = number & 1
        if value == 1:
            count+=1
        number = number>>1
    return count

def selection_matrix(n,r):
    high=pow(2,n)
    matrix=[]
    for i in range(high-1,-1,-1):
        if count_of_1(i) == r:
            matrix.append(i)
    return  matrix

def group_generator(data,r):
    n = len(data)
    matrix = selection_matrix(n,r)
    groups = []
    for number in matrix:
        set = []
        count = 0
        while number != 0:
            value = number & 1
            if value == 1:
                set.append(data[count])
            number = number>>1
            count+=1
        groups.append(set)
    return groups

