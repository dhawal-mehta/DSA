"""
Rearrange the array

Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)].

Rearrange the array such that A[i] = j is changed to A[j] = i for all i and j form 0 to N-1.

Note: Try solving this with O(1) extra space.


Input Format

The only argument given is the integer array A.

Output Format

Return the rearranged array A.

Constraints

1 <= N <= 100000
0 <= A[i] < N

For Example

Input 1:
    A = [1, 2, 3, 4, 0]
Output 1:
    [4, 0, 1, 2, 3]

Input 2:
    A = [2, 0, 1, 3]
Output 2:
    [1, 2, 0, 3]
"""

"""
Hint 1
We can took by using an auxilary array and storing the value one by one.
For this the space complexity will be O(N).
Think of doing it in constant space i.e O(1).
"""
"""
Solution approach
Above solution uses extra space but we can solve this problem without using any extra space by taking advantage of the fact
that array elements lies in the range 0 to n-1.
For each element A[i], we increment value present at index (A[i]%n) by i*n.
Finally, traverse the modified array and set A[i] = A[i]/n.
"""
"""accepted solution"""
# @param A : list of integers
# @return a list of integers
def solve(self, A):

    i = 0
    
    
    currPos = 0
    currNum = A[0]
        
    while i < len(A) :

        
        tempVal = A[currNum]
        
        if tempVal < 0:
            while i<len(A) and A[i] < 0:
                i+=1
            if i <len(A):
                currPos = i
                currNum = A[currPos]
            continue
            
        A[currNum] = currPos - len(A)
        
        currPos = currNum
        currNum = tempVal
        

    for i in range( len(A) ):
        A[i] += len(A)
        
    return A