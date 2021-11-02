"""
K-th character of decrypted string


Problem Description

Given a String A and an integer B. String A is encoded consisting of lowercase English letters and numbers. A is encoded in a way where repetitions of substrings are represented as substring followed by the count of substrings. For example: if the encrypted string is “ab2cd2” and B=4, so the output will be ‘b’ because the decrypted string is “ababcdcd” and 4th character is ‘b’.

You have to find and return the Bth character in the decrypted string.

Note: Frequency of encrypted substring can be of more than one digit. For example, in “ab12c3”, ab is repeated 12 times. No leading 0 is present in the frequency of substring


**Problem Constraints**

1 <= length of the array <= 10^5

1 <= K <= 10^9


**Input Format**

The arguments given are string A and integer B.


**Output Format**

Return the Bth character in the decrypted string.


**Example Input**
Input 1:

    A = "ab2c3"
    B = 5

Input 2:

    A = "x2y3"
    B = 3



**Example Output**
Output 1:

    c

Output 2:

    y



**Example Explanation**

For input 1:Decrypted string will be "ababcccc" and 'c' is the fifth character.

For input 2: Decrypted string will be "xxyyy" and 'y' is the third character."""
"""
Hint 1
We can decode the string and create a new string and then calculate the k-th character but this will cost extra space.Try to solve without using extra space. 
"""
"""
Solution Approach
Find length of current substring. Use two pointers. Fix one pointer at beginning of substring and move another pointer until a digit is not found.

Find frequency of repetition by moving the second pointer further until an alphabet is not found.

Find length of substring if it is repeated by multiplying frequency and its original length.

If this length is less than k, then required character lies in substring that follows. Subtract this length from k to keep count of number of characters that are required to be covered.

If length is less than or equal to k, then required character lies in current substring. As k is 1-indexed reduce it by 1 and then take its mod with original substring length. Required character is kth character from starting of substring which is pointed by first pointer.
"""
# @param A : string
# @param B : integer
# @return a strings
def solve( A, B):
    # stk = []
    
    temp = ""
    offset = B
    i = 0
    length = 0
    while i < len(A):
        str_ = ""
        
        
        while i < len(A) and ord( A[i] ) >= 97:
            str_ += A[i]
            i += 1
        
        
        
        num = ""
        # print(i,str_,ord(A[i]))
        
        while i < len(A) and ord(A[i]) < 97:
            num += A[i]
            i+=1



        length += len(str_)*int(num)

        if length >= B:
            break
        
        offset -= len(str_)*int(num)
    
    
    return str_[ (offset-1)% len(str_) ]
