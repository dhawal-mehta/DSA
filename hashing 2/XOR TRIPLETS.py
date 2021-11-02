"""XOR TRIPLETS

Problem Description

Given an array of integers A of size N.

A triplet (i, j, k), i <= j <= k is called a power triplet if A[i] ^ A[i+1] ^....A[j-1] = A[j] ^.....^A[k].

Where, ^ denotes bitwise xor.

Return the count of all possible power triplets. Since the answer could be large return answer % 109 +7.



Problem Constraints

1 <= N <= 100000
1 <= A[i] <= 100000


Input Format

The first argument given is the integer array A.


Output Format

Return the count of all possible power triplets % 109 + 7.


Example Input

Input 1:

 A = [5, 2, 7]

Input 2:

 A = [1, 2, 3]



Example Output

Output 1:

 2

Output 2:

 2



Example Explanation

Explanation 1:

 All possible power triplets are:
    1. (1, 2, 3) ->  A[1] = A[2] ^ A[3]
    2. (1, 3, 3) ->  A[1] ^ A[2] = A[3]

Explanation 2:

 All possible power triplets are:
    1. (1, 2, 3) ->  A[1] = A[2] ^ A[3]
    2. (1, 3, 3) ->  A[1] ^ A[2] = A[3]
"""
"""
Hint 1
Can we say that to calculate answer we need to find the subarrays such that Xor of that subarray is Zero.
"""
"""
Solution Approach

A simple is to find the every possible triplet and check if it satisfies the above condition.
But this is not an efficient way to do that.

One thing we observe is that for (i,j,k), A[i]^A[i+1]..^A[j-1] = A[j]^A[j+1]^A[k] i.e A[i]^A[i+1]..^A[k] = 0.
So, if we find (i,k) such that A[i]^A[i+1]..^A[k] = 0, then all j in this range will satisfy our above condition.

An efficient solution is to use Trie.

-> We will take the cumulative xor of the elements in the array and check that this xor value exists in the Trie or not.

-> If the xor already exists in the Trie then we have encounted a subarray having 0 xor and count all the triplets.

-> Else push the value of xor into the Trie.

"""
# @param A : list of integers
# @return an integer
def solve(A):        
    store = {}
    store[0] = [-1]
    currXOR = 0
    count = 0
    for i in range(len(A)):
        # print(currXOR, count)
        currXOR ^= A[i]
        if currXOR in store:
            for pos in store[currXOR]:
                count = (count + (i-pos-1) )%1000000007
            
            store[currXOR].append(i)
        else:
            store[currXOR] = [i]
    
    return count
