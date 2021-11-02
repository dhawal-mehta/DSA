"""Reduce the string


Given a string A consisting of lowercase English alphabets. Reduce the string to its shortest length by doing any number of operations (possibly zero). In one operation selects a pair of adjacent letters in the string that match and deletes them. For example the string bcaa is shortened to bc in one operation.

Find and return the string by reducing it to its shortest length. if the resultant string is empty return "empty".


Input Format

The only argument given the string A.

Output Format

Return the string by reducing it to its shortest length. if the resultant string is empty return "empty".

Constraints

1 <= length of the string <= 1000000

For Example

Input 1:
    A = "aaabccddd"
Output 1:
    "abd"

Input 2:
    A = baab
Output 2:
    "empty"
"""
# @param A : string
# @return a strings
def solve( A):
    
    stk = []
    for i in A:
        if len(stk) == 0:
            stk.append(i)
        else:
            if stk[-1] == i:
                stk.pop()
            else:
                stk.append(i)
    
    # print(stk)
    ans = "".join(stk)
    if len(ans) == 0:
        return "empty"
        
    return ans 