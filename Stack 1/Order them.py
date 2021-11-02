"""
 Order them

Problem Description

Given an array of integers A describing ranking of trucks. Your task is to insert these rank in another array B by some means of operations such that B is sorted in ascending order. For performing these operations you can use one stack C.

In one Operation you can perform any of the following steps:

    Remove the first element from A and append at the back of C.
    Remove the last element from C and append at the back of B.
    Remove the first element from A and append at the back of B.

you can perform these operations any number of times (possibly zero).

Return 1 if B can be formed in ascending order using some operations else return 0.



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= length of Array
All elements of A are distinct.


Input Format

The only argument given is the integer array A.


Output Format

Return 1 if B can be formed in ascending order using some operations else return 0.


Example Input

Input 1:

A = [5, 1, 2, 4, 3]

Input 2:

A = [5, 3, 1, 4, 2]



Example Output

Output 1:

1

0



Example Explanation

Explanation 1:

Given array A = [5, 1, 2, 4, 3], stack C = [] , array B = []
step 1: A = [5, 1, 2, 4, 3]
        C = []
        B = []
step 2: A = [1, 2, 4, 3]
        C = [5]
        B = []
step 3: A = [2, 4, 3]
        C = [5]
        B = [1]
step 4: A = [4, 3]
        C = [5]
        B = [1, 2]
step 5: A = [3]
        C = [5, 4]
        B = [1, 2]
step 6: A = []
        C = [5, 4]
        B = [1, 2, 3]
step 7: A = []
        C = [5]
        B = [1, 2, 3, 4]
step 8: A = []
        C = []
        B = [1, 2, 3, 4, 5]
Array B is in ascending order. So, return 1.
"""
"""
Hint 1
We can only remove first element from A.

Now, the only thing left is whether to append element to the stack or to the array B.

"""
"""
Solution Approach

If we append wrong element at the back of B, then it will not be possible to form array B ascending as we can only append element at the back.

Therefore, we will append element at the back of B in incremental fashion starting from 1.

If we can’t append element at the back of B, then the only option is to append at the back of stack C.

Try to simulate the problem. If at any time the number which is to be added to B is not at front of A or at the back of stack, then B can’t be formed in ascending order.
"""
# @param A : list of integers
# @return an integer
def solve(self, A):
    stk = []
    B = []
    first = min(A)
    N = len(A)
    i = 0
    while i < N and A[i] != first:
        stk.append(A[i])
        i += 1
    
    B.append(A[i])
    i +=1
    
    while i < N:
        if not stk:
            stk.append(A[i])
            i+=1
            
        elif A[i] <= stk[-1]:
            stk.append(A[i])
            i+=1
        else:
            B.append(stk.pop())
    
    for temp in range(len(stk)):
        B.append(stk.pop())
    
    # print(stk)
    # print(B)
    for i in range(N-1):
        if  B[i] > B[i+1]:
            return 0
    
    return 1
            