"""
Maximum Difference

Given an array of integers A and an integer B. Find and return the maximum value of ** 	s1 - s2 	**

where s1 = sum of any subset of size B, s2 = sum of elements of A - sum of elemets of s1
Note ** 	x 	** denotes the absolute value of x.



Input Format

The arguments given are the integer array A and integer B.

Output Format

Return the maximum value of | s1 - s2 |.

Constraints

1 <= B < length of the array <= 100000
1 <= A[i] <= 10^5 

For Example

Input 1:
    A = [1, 2, 3, 4, 5]
    B = 2
Output 1:
    9

Input 2:
    A = [5, 17, 100, 11]
    B = 3
Output 2:
    123

"""
"""
Hint 1
We have to find the maximum value of |s1-s2|.
Now for to maximize any absolute value 2 conditions are there:
1st cond.-> s1 should be max as possible and s2 should be min. as possible.
2nd cond.-> s2 should be min as possible and s1 should be max as possible.
"""
"""
Solution Approach
We have to find the maximum value of |s1-s2|.
Now for to maximize any absolute value 2 conditions are there:
1st cond.-> s1 should be max as possible and s2 should be min. as possible.
2nd cond.-> s2 should be min as possible and s1 should be max as possible.

Now in this question there is a mandatory condition we have to take any subset of B size.
So for 1st condition if we try to take maximize the value of s1 . so take only 'B' large values 
and for 2nd condition try to take 'B' small values.
Time Complexity; Nlog N

NOTE: to find small values and large values . Sort the given array.
"""
# @param A : list of integers
# @param B : integer
# @return an integer
def solve(A, B):
    
    max_ = -1
    n = sum(A)
    A = sorted(A)
    
    sum_1= abs(sum( A[:B] )*2 - n) 
    
    temp = A[::-1]
    
    sum_2= abs(sum( temp[:B] )*2 - n) 
    
            
    return max(sum_1,sum_2 )
    # return max_

