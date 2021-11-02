"""Longest Substring Without Repeat

Problem Description

Given a string A, find the length of the longest substring without repeating characters.

Note: Users are expected to solve in O(N) time complexity.



Problem Constraints

1 <= size(A) <= 106

String consists of lowerCase,upperCase characters and digits are also present in the string A.



Input Format

Single Argument representing string A.


Output Format

Return an integer denoting the maximum possible length of substring without repeating characters.


Example Input

Input 1:

 A = "abcabcbb"

Input 2:

 A = "AaaA"



Example Output

Output 1:

 3

Output 2:

 2



Example Explanation

Explanation 1:

 Substring "abc" is the longest substring without repeating characters in string A.

Explanation 2:

 Substring "Aa" or "aA" is the longest substring without repeating characters in string A.
"""
"""
Hint 1

Think in terms of two pointers.
If you encounter a repeating character, you won’t be able to include the new character till you exclude out the previous 
occurrence of the character. Which means your window needs to shrink till your start character is pointing to the position 
next to previous occurrence of the character.
"""
"""
Solution Approach

All you need to do is use two pointers to keep a window with no repetitions of characters. Keep moving the right pointer and if you encounter any repeating character start moving left pointer untill no character is repeated.

Also, note that the size of character set is small ( 128 at max ), so tracking the count of characters in the current set is fairly easy using hashing / array buckets.
"""
# @param A : string
# @return an integer
def lengthOfLongestSubstring(A):
    start = 0
    end = 0
    
    foundSet = set()
    maxLength = 0
    
    while end < len(A):
        
        if A[end] in foundSet:
            while A[start] != A[end]:
                foundSet.remove(A[start])
                start+=1
            start+=1
        else:
            maxLength = max( maxLength, end-start+1)
            foundSet.add( A[end] )
        
        
        end+=1
    
    # print(foundSet)
    return maxLength


