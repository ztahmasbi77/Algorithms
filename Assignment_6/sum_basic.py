from math import inf
def minSubsetDifference_recursive(N, s_list): 
    difference=0
    sum=0
    compare=[]
    for i in range(len(s_list)):
        sum+=s_list[i]
        if sum == N:
            return difference
        if sum > N:
            for j in range(i+1):
                compare.append(minSubsetDifference_recursive(sum-N,s_list[:j]))
                difference=min(compare)
    if sum < N:
        return 1+minSubsetDifference_recursive(N-1,s_list)
    return difference

print(minSubsetDifference_recursive(15, [1, 2, 3, 4, 5, 10])) # Should be zero
print(minSubsetDifference_recursive(26, [1, 2, 3, 4, 5, 10])) # should be 1
print(minSubsetDifference_recursive(23, [1, 2, 3, 4, 5, 10])) # should be 0
print(minSubsetDifference_recursive(18, [1, 2, 3, 4, 5, 10])) # should be 0
print(minSubsetDifference_recursive(9, [1, 2, 3, 4, 5, 10])) # should be 0
