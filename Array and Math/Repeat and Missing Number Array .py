"""
    Repeat and Missing Number Array


    You are given a read only array of n integers from 1 to n.

    Each integer appears exactly once except A which appears twice and B which is missing.

    Return A and B.

    Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Note that in your output A should precede B.

    Example:

        Input:[3 1 2 5 3] 

        Output:[3, 4] 

        A = 3, B = 4

"""

"""  solution 1  
     we can solve this without changing the array


arr = [3, 1, 2, 5, 3] 

def swap (p1,p2):
    arr[p1] ,arr[p2] = arr[p2],arr[p1]
A=0
i= 0
while i < len(arr):
    
    if arr[i] == i+1:
        i+=1
    else:
        if arr[i] == arr[arr[i]-1]:
            A = arr[i]
            i = len(arr)
            break

        swap(i,arr[i]-1)

# print(A)
BminusA = ( len(arr)*(len(arr)+1)//2 ) - sum(arr)
print(A, BminusA + A)

"""

""" accepted solution """

# @param A : tuple of integers
# @return a list of integers
def repeatedNumber( A):
    n=len(A)
    sum=0
    squared_sum=0

    for num in A:
        sum+=num
        squared_sum+=num*num
    # print(sum,squared_sum)

    ideal_sum=(n*(n+1))//2
    ideal_squared_sum=(n*(n+1)*(2*n+1))//6
    # print(ideal_sum,ideal_squared_sum)

    sum_diff=ideal_sum-sum
    squared_sum_diff=ideal_squared_sum-squared_sum

    b=(sum_diff+(squared_sum_diff//sum_diff))//2
    a=b+sum-ideal_sum
    return [a,b]




