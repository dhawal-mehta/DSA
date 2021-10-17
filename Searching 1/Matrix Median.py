"""Matrix Median

Problem Description

Given a matrix of integers A of size N x M in which each row is sorted.

Find and return the overall median of the matrix A.

NOTE: No extra memory is allowed.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

1 <= N, M <= 10^5

1 <= NM <= 10^6

1 <= A[i] <= 10^9

NM is odd



Input Format

The first and only argument given is the integer matrix A.


Output Format

Return the overall median of the matrix A.


Example Input

Input 1:

A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ]

Input 2:

A = [   [5, 17, 100]    ]



Example Output

Output 1:

 5

Output 2:

 17



Example Explanation

Explanation 1:

 
A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5.

Explanation 2:

 
Median is 17.
"""
"""
Hint 1

We cannot use extra memory, so we can’t actually store all elements in an array and sort the array.
But since, rows are sorted it must be of some use, right?

Note that in a row you can binary search to find how many elements are smaller than a value X in O(log M).

"""
"""
Solution Approach

We cannot use extra memory, so we can’t actually store all elements in an array and sort the array.
But since, rows are sorted it must be of some use, right?

Note that in a row you can binary search to find how many elements are smaller than a value X in O(log M).
This is the base of our solution.

Say k = N*M/2. We need to find (k + 1)^th smallest element.
We can use binary search on answer. In O(N log M), we can count how many elements are smaller than X in the matrix.

So, we use binary search on interval [1, INT_MAX]. So, total complexity is O(30 * N log M).

Note:
This problem can be solve by using min-heap, but extra memory is not allowed.

"""
# @param A : list of list of integers
# @return an integer
def getLessMore( A, num):
    x1 = 0
    x2 = 0
    for row in A:
        for i in row:
            if i < num:
                x1 += 1
                
            elif i > num:
                x2 += 1
    return x1,x2
    
def util(A, N,min_,max_):
    mid_ = (min_ + max_ )//2
    x1,x2 = getLessMore(A,mid_)
    start = x1
    end = N - (x2 + 1)
    
    if x1 + x2 == N: #this will handle mid_ not present
        # print("not Found")
        # return -1
        # do something here 
        if start > N//2:
            return util(A,N,min_,mid_-1)
        else:
            return util(A, N, mid_+1, max_)
            
    if start<=N//2 and end>=N//2:
        return mid_      
    
    elif end < N//2:
        return util(A, N, mid_+1, max_)
    
    elif start > N//2:
        return util(A, N, min_, mid_-1)
        
def findMedian( A):
    min_ = A[0][0]
    max_ = A[0][0]
    
    for row in A:
        for i in row:
            if i<min_:
                min_ = i
                
            if i>max_:
                max_ = i
    
    # print(max_, min_)
    # return 0
    
    return util(A,len(A)*len(A[0]) ,min_,max_)
