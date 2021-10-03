"""Count of paths in a grid


Given an integer A, find and return the
number of paths in a grid of size (A x A) that starts from (1, 1) and reaches (A, A) without crossing the major diagonal.

Since the result can be large, return the result modulo (10^9 + 7).

NOTE: The major diagonal of a matrix A is the collection of entries A[i][j] where i == j



Input Format

The only argument given is integer A.

Output Format

Return the number of paths modulo (10^9 + 7).

Constraints

1 <= A <= 10^6

For Example

Input 1:
    A = 2
Output 1:
    1

Input 2:
    A = 5
Output 2:
    14

"""

"""
Solution approach
This is N'th catalan's number
"""

# -------------------------------------- this is O(n^2) ---------------------------------------------------
def solve( A):
    A=A-1
    count = [0]*(A+1)
    count[0] = 1
    count[1] = 1
    for i in range(2,A+1):
        for j in range(0,i):
            count[i] = ( count[i] + count[j]*count[i-1-j] )%(10**9 + 7)

    
    return count[A]

# --------------------------------------- this is O(n) -------------------------------------------------------
def binomialCoefficient(n, k):
    # since C(n, k) = C(n, n - k)
    # we are going till smaller one. why should we waste time and go till larger one.
    if (k > n - k):
        k = n - k
 
    
    res = 1
 
    # Calculate value of [n * (n-1) *---* (n-k + 1)]
    # / 1*2*3...k
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res
 
def solve(n):
    c = binomialCoefficient(2*n, n)
    return c/(n + 1)
 