"""Find Rectangle in binary matrix

Problem Description

Given a binary matrix of integers A of size N x M consisting of only 0 or 1. you need to check whether there exists a square or rectangle in a square whose all four corners are 1. All four corners need to be distinct.

If there exists such rectangle or square return 1, else return 0.

Input Format The first argument given is the integer matrix A. Output Format Return 1 if there exists such rectangle/square whose all four corners are 1 else return 0. Constraints 1 <= N, M <= 200 0 <= A[i] <= 1 For Example ``` Input 1: A = [ [0, 1, 1] [0, 1, 1] [0, 1, 0] ]

Output 1: 1

Explanation 1: [ [1, 1] [1, 1] ] There exists a square whose all corners are 1.

Input 2: A = [ [0, 1, 1] [0, 0, 1] [0, 1, 0] ]

Output 2: 0 """
"""
Solution Approach

1. Scan from top to down, line by line.
2. For each line, remember each combination of 2 1’s and push that into a hash-set.
3. If we ever find that combination again in a later line, we get our rectangle.

Time Complexity: O(N * M^2)
"""
# @param A : tuple of list of integers
# @return an integer
def solve(A):
    
    hash = []
    hashSet = set()
    
    for i in range( len(A) ):
        hash.append([])
        for j in range( len(A[0]) ):
            
            if A[i][j] == 1:
                hash[-1].append( j )
                hashSet.add(i*len(A[0]) + j)

    row = len(A)
    col = len(A[0])
    # print(hashSet)
    for i in range( len(hash) ) :
        for j in range(1,len( hash[i] ) ):
            num1 = hash[i][j-1]
            num2 = hash[i][j]
            # print(i, j, num1, num2)
            for k in range(i+1, len(hash)):
                if num1 + k*col in hashSet and num2 + k*col in hashSet:
                    return 1

            
    return 0