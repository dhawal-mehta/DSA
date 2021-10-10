"""
Xor queries

Problem Description
You are given an array A (containing only 0 and 1) as element of N length.

Given L and R, you need to determine value of XOR of all elements from L to R (both inclusive) and number of unset bits (0's) in the given range of the array.


Problem Constraints

1<=N,Q<=100000
1<=L<=R<=N



Input Format

First argument contains the array of size N containing 0 and 1 only. 
Second argument contains a 2D array with Q rows and 2 columns, each row represent a query with 2 columns representing L and R.



Output Format

Return an 2D array of Q rows and 2 columns i.e the xor value and number of unset bits in that range respectively for each query.



Example Input

A=[1,0,0,0,1]
B=[ [2,4],
    [1,5],
    [3,5] ]



Example Output

[[0 3]
[0 3]
[1 2]]



Example Explanation

In the given case the bit sequence is of length 5 and the sequence is 1 0 0 0 1. 
For query 1 the range is (2,4), and the answer is (array[2] xor array[3] xor array[4]) = 0, and number of zeroes are 3, so output is 0 3. 
Similarly for other queries.
"""
"""
Hint 1
We kow that XOR operation has a property that xor(a,a) = 0 i.e a^a = 0. So xoring a number with itself gives 0.
Try to use this property to get the answer.
"""
"""
Solution Approach
We know x^x=0 and x^0=x where ‘^’ is the symbol for xor operation.

You should store the cumulative xor value for index i in array A i.e. A[i] will have the xor value of all the elements from 1 to i (boundary included).

You should also store the total number of ones or zeroes scanned till now, in another array say B i.e. B[i] will tell the total number of ones/zeroes from 1 to i(both inclusive).

Therefore now, xor value from L to R is A[R]^A[L-1] because, A[R] has xor values of elements from 1 to R which includes xor of 1 to L-1 and L-1 to R.

Therefore, if we take xor of A[L-1] with A[R] then, we will nullify the affect of all elements from 1 to L-1, resulting in the output of xor values from L to R.

For total number of ones/zeroes.you simply do B[R]-B[L-1].
"""
# @param A : list of integers
# @param B : list of list of integers
# @return a list of list of integers
def solve( A, B):
    n=len(A)
    pre=[0]*(n+1)
    for i in range(n):
        pre[i+1]+=pre[i]
        pre[i+1]+=A[i]
    ans=[]
    m=len(B)
    for i in range(m):
        l=B[i][0]
        r=B[i][1]
        ones=pre[r]-pre[l-1]
        xor=0
        if(ones%2):
            xor=1
        ans.append([xor,r-l+1-ones])
    return ans    