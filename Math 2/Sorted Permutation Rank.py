"""Sorted Permutation Rank


Problem Description

Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

Note: The answer might not fit in an integer, so return your answer % 1000003



Problem Constraints

1 <= |A| <= 1000


Input Format

First argument is a string A.


Output Format

Return an integer denoting the rank of the given string.


Example Input

Input 1:

A = "acb"

Input 2:

A = "a"



Example Output

Output 1:

2

Output 2:

1



Example Explanation

Explanation 1:

Given A = "acb".
The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
So, the rank of A is 2.

Explanation 2:

Given A = "a".
Rank is clearly 1."""
"""
Hint 1
Enumerating all permutations and matching with the current one is going to be exponential.

Lets start by looking at the first character.

If the first character is X, all permutations which had the first character less than X would come before this permutation when sorted lexicographically.

Number of permutation with a character C as the first character = number of permutation possible with remaining N-1 character = (N-1)!

Can you use the above information to get the rank of the current permutation ?
"""
"""
Solution Approach
Lets start by looking at the first character.

If the first character is X, all permutations which had the first character less than X would come before this permutation when sorted lexicographically.

Number of permutation with a character C as the first character = number of permutation possible with remaining N-1 character = (N-1)!

Then the problem reduces to finding the rank of the permutation after removing the first character from the set.

Hence,

rank = number of characters less than first character * (N-1)! + rank of permutation of string with the first character removed

Example

Lets say out string is “VIEW”.

Character 1 : 'V'
All permutations which start with 'I', 'E' would come before 'VIEW'.
Number of such permutations = 3! * 2 = 12

Lets now remove ‘V’ and look at the rank of the permutation ‘IEW’.

Character 2 : ‘I’
All permutations which start with ‘E’ will come before ‘IEW’
Number of such permutation = 2! = 2.

Now, we will limit ourself to the rank of ‘EW’.

Character 3:
‘EW’ is the first permutation when the 2 permutations are arranged.

So, we see that there are 12 + 2 = 14 permutations that would come before "VIEW".
Hence, rank of permutation = 15.
"""
""" Accepted solution """
#for char i you find number of char that have ord less then curr char
#then add ( [pos of curr char ] - 1 )! to the ans 
def findRank(A):
    MOD = 1000003
    N = len(A)
    def fact(n):
        return n*fact(n-1) if n != 1 else 1
    
    def getSmaller(A, curr):
        count = 0
        for i in range(curr+1, len(A)):
            if ord(A[curr]) > ord(A[i]):
                count += 1
        return count
    
    factA = fact(N)
    
    ans = 1
    for i in range(N-1):
        factA = factA//(N-i)
        
        temp = getSmaller(A, i)
        
        ans = (ans + factA*temp)%MOD
        
    return ans 
