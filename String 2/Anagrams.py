"""
Anagrams


Problem Description

Given an array A of N strings, return all groups of strings that are anagrams.

Represent a group by a list of integers representing the index(1-based) in the original list. Look at the sample case for clarification.

NOTE: Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'.



Problem Constraints

1 <= N <= 104

1 <= |A[i]| <= 104

Each string consists only of lowercase characters.

Sum of length of all the strings doesn't exceed 107



Input Format

Single Argument A which is an array of strings.


Output Format

Return a two-dimensional array where each row describes a group.

Note:

Ordering of the result :
You should not change the relative ordering of the strings within the group suppose within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.



Example Input

Input 1:

 A = [cat, dog, god, tca]

Input 2:

 A = [rat, tar, art]



Example Output

Output 1:

 [ [1, 4],
   [2, 3] ]

Output 2:

 [ [1, 2, 3] ]



Example Explanation

Explanation 1:

 "cat" and "tca" are anagrams which correspond to index 1 and 4 and "dog" and "god" are another set of anagrams which correspond to index 2 and 3.
 The indices are 1 based ( the first element has index 1 instead of index 0).

Explanation 2:

 All three strings are anagrams."""

"""
Hint 1

Anagrams will map to the same string if the characters in the string are sorted.
Can you use the above fact to come up with a strategy ?
"""
"""
Solution Approach

Anagrams will map to the same string if the characters in the string are sorted.
We can maintain a hashmap with the key being the sorted string and the value being the list of strings ( which have the sorted characters as key ).
"""
# @param A : tuple of strings
# @return a list of list of integers
def anagrams( A):
    s = {}
    for i in range( len(A) ):
        word = ''.join(sorted(A[i]))
        # print(A[i], word)
        if word not in s:
            s[word] = [i+1]
        else:
            s[word].append(i+1)
    
    return( list( s.values() ) )