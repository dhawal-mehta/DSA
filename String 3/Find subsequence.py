"""
Find subsequence


Given two strings A and B, find if A is a subsequence of B.

Return "YES" if A is a subsequence of B, else return "NO".


Input Format

The first argument given is the string A.
The second argument given is the string B.

Output Format

Return "YES" if A is a subsequence of B, else return "NO".

Constraints

1 <= lenght(A), length(B) <= 100000
'a' <= A[i], B[i] <= 'z'

For Example

Input 1:
    A = "bit"
    B = "dfbkjijgbbiihbmmt"
Output 1:
    YES

Input 2:
    A = "apple"
    B = "appel"
Output 2:
    "NO"
"""
# @param A : string
# @param B : string
# @return a strings
def solve(self, A, B):
    ptr1 = 0
    ptr2 = 0
    
    while ptr1 < len(A) and ptr2 < len(B):
        if A[ptr1] == B[ptr2]:
            ptr1 += 1
            ptr2 += 1
        else:
            ptr2 +=1
    
    if ptr1 == len(A):
        return "YES"
    else:
        return "NO"