"""
Reverse the String


Problem Description

Given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

    A sequence of non-space characters constitutes a word.
    Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
    If there are multiple spaces between words, reduce them to a single space in the reversed string.



Problem Constraints

1 <= N <= 3 * 105


Input Format

The only argument given is string A.


Output Format

Return the string A after reversing the string word by word.


Example Input

Input 1:
    A = "the sky is blue"

Input 2:
    A = "this is ib"  



Example Output

Output 1:
    "blue is sky the"

Output 2:
    "ib is this"    



Example Explanation

Explanation 1:
    We reverse the string word by word so the string becomes "the sky is blue".

Explanation 2:
    We reverse the string word by word so the string becomes "this is ib".
"""
"""
Hint 1
This is just a brute force problem which can be simulated in one or two pass of the main string.

Try to focus on the words(begining and ending positions) instead of extra spaces.

"""
"""
Solution Approach

One simple approach is a two-pass solution:

    First pass to split the string by spaces into an array of words
    Then second pass to extract the words in reversed order

We can do better in one-pass. While iterating the string in reverse order, we keep track of a word’s beginning and end position.

When we are at the beginning of a word, we append it.

"""
# @param A : string
# @return a strings
def solve( A):
    temp = A.split(" ")
    i = -1
    while len(temp[i]) == 0:
        i-=1

    # print(temp)
    if i+1<0:
        temp = temp[:i+1]

    # print(i)
    # print(temp)
    str_ = " ".join( temp[::-1] )
    # print(str_)
    return str_