"""
Regroup 0's and 1's using Minimum Swaps


Given a string S, count minimum no. of swaps needed to regroup 0's and 1's.

After all swaps final string will look like all 0's followed by all 1's or all 1's followed by all 0's.

Swap operation swaps two adjacent characters (01 -> 10, 10 -> 01, 00 -> 00 and 11 -> 11).

Note:

    Try to solve the problem using constant extra space. Expected time complexity is worst case O(length of S).

Examples:

S: 000111 Answer: 0

S: 1110101 Answer: 3 Explanation: 1110101 -> 1111001 -> 1111010 -> 1111100
"""
"""
Hint 1
We have two options either we make final string look like all 0s followed by all 1s or all 1s followed by all 0s. So, simply we can consider both and return minimum of them.

While considering either of the cases think about the difference in position of initial and final 0s and 1s.

"""
"""
Solution Approach
Suppose we want to make 111000 from S = 101001. Then 1s in S with position 1, 3 and 6 will go to position 1, 2 and 3 in final ans.
 So, ans is simply (1 - 1) + (3 - 2) + (6 - 3) = 0 + 1 + 3 = 4 that can be calculated with one pass and constant extra space.

So, if you observe for decreasingly sorted string like 11..00 you will swap 1 in S equal to number of 0’s before current 1, iterating from most significant bit to least significant bit. Similarly for increasingly sorted string 001111 you will swap 0 in S equal to number of 1’s before current 0, iterating from most significant bit to least significant bit.

"""
# @param A : string
# @return an integer
def solve( A):
    
    OneCount = 0
    swapCount = 0
    for i in range(len(A)):
        # print(i)
        if A[i] == '0':
            swapCount += OneCount
        else:
            OneCount += 1
    temp = swapCount
    
    OneCount = 0
    swapCount = 0
    for i in range(len(A),-1,-1):
        if A[i] == '0':
            swapCount += OneCount
        else:
            OneCount += 1
    
    return min(temp, swapCount)