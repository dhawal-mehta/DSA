"""
Make String Pallindrome


Problem Description

Given a string A of size N consisting only of lowercase alphabets. The only operation allowed is to insert characters in the beginning of the string.

Find and return how many minimum characters are needed to be inserted to make the string a palindrome string.



Problem Constraints

1 <= N <= 106


Input Format

The only argument given is a string A.


Output Format

Return an integer denoting the minimum characters that are needed to be inserted to make the string a palindrome string.


Example Input

Input 1:

 A = "abc"

Input 2:

 A = "bb"



Example Output

Output 1:

 2

Output 2:

 0



Example Explanation

Explanation 1:

 Insert 'b' at beginning, string becomes: "babc".
 Insert 'c' at beginning, string becomes: "cbabc".

Explanation 2:

 There is no need to insert any character at the beginning as the string is already a palindrome. 
"""
"""
Hint 1
Try to lea rn about LPS array used in KMP string matching algorithm. 

Modify your string and compute its LPS array to derive the answer.
"""
"""
Solution Approach

Each index of LPS array contains the longest prefix which is also a suffix. Now take the string and 
reverse of a string and combine them with a sentinal character in between them and compute the LPS array of this 
combined string. Now take the last value of the LPS array and subtract it with the length of the original string, 
This will give us the minimum number of insertions required in the begining of the string . 
"""
# @param A : string
# @return an integer
def solve( A):
    fwd = 0
    back = len(A)-1
    count = 0
    
    str_ = A +  '$' + A[::-1]
    
    lps = [0]*len(str_)
    
    start = 0
    end = 1
    while end < len(str_):
        if str_[start] == str_[end]:
            lps[end] = start + 1
            end += 1
            start += 1
        else:
            if start == 0:
                lps[end] = 0
                end += 1
            else:
                start = lps[start-1]

    
    return len(A) - lps[-1] 