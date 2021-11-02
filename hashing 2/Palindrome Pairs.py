"""
Palindrome Pairs

Problem Description

Given a list of unique words A, find all pairs of distinct indices (i, j) in the given list such that concatenation of the two words, i.e. A[i] + A[j] is a palindrome.

Note: A string is a palindrome if it reads the same backward as forward.



Problem Constraints

1 <= length of the list A <= 1000

1 <= lenght of words in list A <= 100



Input Format

The only argument given is the string array A.


Output Format

Return the list of all pairs of distinct indices such that concatenation of the two words, i.e. A[i] + A[j] is a palindrome.

You can return the list in any order.



Example Input

Input 1:

 A = ["abcd", "dcba", "lls", "s", "sssll"]

Input 2:

 A =  ["bat", "tab", "cat"]



Example Output

Output 1:

 [ [0,1], [1,0], [3,2], [2,4] ]

Output 2:

 [[0,1],[1,0]] 



Example Explanation

Explanation 1:

 The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Explanation 2:

 The palindromes are ["battab","tabbat"]
"""
"""
Hint 1

Given: No duplicated string in the list.

Let N = length of the list.

let K = max length of the word in the list.

Approach 1:

Run two loops one for i and one for j and check if concatenation of A[i] and A[j] i.e. A[i]+A[j] is palindrome.
Time Complexity= KN^2

This will be sufficient for N=100 but for higher N it will lead to TLE.
Think of a more efficient approach.

"""
"""
Hint 2
Given: No duplicated string in the list.

Let N = length of the list.

let K = max length of the word in the list.

Approach 2(Optimized):

    Traverse the array, build map. Key is the reversed string, value is index in array (0 based)

    Main logic part. Partition the word into left and right, and see
        if there exists a candidate in map equals the left side of current word, and right side of current word is palindrome, so concatenate(current word, candidate) forms a pair: left | right | candidate.
        same for checking the right side of current word: candidate | left | right.
"""
"""
Solution Approach
It can be solved by trie data strcuture, as we have to find whether two strings after concatenating can become a palindrome or not.
We insert all words in reverse in trie.. So if there is a A[i] and we break it into two parts , say left and right A[l] and A[r] so if A[l] is present in trie that means there is a word present which after reversing equals to A[l] so that reverse(founded_word)== A[l] and A[r] is a palindrome then we can append founded_word at the end of current word like this -:: A[l] + A[r] + founded_word and it can be easily determined that it is a palindrome.
So idea is clear , now use trie to reduce time for searching and inserting..
That’s it… Hope u understand!!

"""
# @param A : list of strings
# @return a list of list of integers
def isPalindrome( str_, start, end):
    if start >= end:
        return True
    
    for i in range( 0, (end - start)//2+1):
        # print(str_,start, i ,end)
        # print(str_[start+i])
        if str_[start + i] != str_[end-i]:
            return False
            
    return True
    
def solve(self, A):
    
    hash = {}
    for i in range(len(A)):
        hash[ A[i] ] = i
    
    ans= set()
    for i in range( len(A) ):
        word = A[i]
        # print("***  starts")
        for j in range(1,len(word)+1):
            try:
                prefix =  word[:j]
                prefix = prefix[::-1]
                # print("search for prefix", prefix)
                # print("palindrome for",word[j:])
                temp = hash[prefix]
                
            except:
                temp= -1
                # print("prefix bot",prefix ,j)
                
            if i != temp and temp != -1 and self.isPalindrome(word, j ,len(word)-1 ):
                # print("pre",prefix,word[j:],self.isPalindrome(word, j ,len(word)-1 ))
                ans.add( (i, temp ) )
            
            # print("---")
            
            try:
                # print("test")
                
                suffix = word[len(word) - j:]
                suffix = suffix[::-1]
                # print(word, suffix)
                # print("search for suffix ", suffix)
                temp = hash[suffix]
            
            except:
                temp = -1
            
            if i != temp and temp != -1 and self.isPalindrome(word, 0, len(word)-j-1):
                # print("suff",suffix,word[0:len(word)-j-1])
                ans.add( (temp, i) )
            
    
    return list(ans)