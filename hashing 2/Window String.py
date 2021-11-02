"""
Window String


Problem Description

Given a string A and a string B, find the window with minimum length in A which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in minimum window in A should be at least x.

Note:

    If there is no such window in A that covers all characters in B, return the empty string.
    If there are multiple such windows, return the first occurring minimum window ( with minimum start index )



Problem Constraints

1 <= size(A), size(B) <= 106


Input Format

First argument is a string A.
Second argument is a string B.


Output Format

Return a string denoting the minimum window.


Example Input

Input 1:

 A = "ADOBECODEBANC"
 B = "ABC"

Input 2:

 A = "Aa91b"
 B = "ab"



Example Output

Output 1:

 "BANC"

Output 2:

 "a91b"



Example Explanation

Explanation 1:

 "BANC" is a substring of A which contains all characters of B.

Explanation 2:

 "a91b" is the substring of A which contains all characters of B.
 
 """
"""
Hint 1

Think 2 pointers and hashing.

How can you move left and right pointers in order to fit all the characters of B?
"""
"""
Solution Approach

Essentially you have a start and end pointer starting from the beginning of the string.

You keep moving the end pointer and including more characters till you have all the characters of B included.

At this point, you start moving start pointer and popping out characters till the point that you still have all the characters of B included. Update your answer and keep repeating the process.
"""
# @param A : string
# @param B : string
# @return a strings
def minWindow(A, B):
    
    if len(A) < len(B):
        return ""
        
    found = {}
    hash = {}
    lenFound = 0
    for i in B:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
        
    start = 0
    end = 0
    
    ans = len(A)+1
    startAns = 0
    endAns = 0
    
    
    while end < len(A):
        if A[end] in hash:
            if A[end] not in found:
                found[ A[end] ] = 1
                lenFound += 1
            else:
                found[A[end]]  += 1
                if found[ A[end] ] <= hash[ A[end] ]:
                    lenFound += 1
                
            flag = True
            while flag and start < len(A):
    
                if  A[start] in found and found[ A[start] ] > hash[ A[start] ]:
                    
                    found[ A[start] ] -= 1
                    start += 1
                
                elif A[start] not in hash:
                    start += 1
                    # lenFound -= 1
    
                else:
                    flag = False
            
            if lenFound == len(B)and A[end] in hash and end-start+1 < ans:
                ans = end-start+1
                startAns = start
                endAns = end
        
        end += 1
        
        
    if ans <= len(A) and lenFound == len(B):
        return A[startAns:endAns+1]
    else:
        return ""