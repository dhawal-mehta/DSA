"""
Subarrays Xor Less Than B


Problem Description
Given an array of integers A. Find and return the number of subarrays whose xor values is less than B.

NOTE: As the answer can be very large, return the answer modulo (109+7).



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 105
1 <= B <= 106


Input Format

The argument given is the integer array A
Second argument is an integer B.


Output Format

Return an integer denoting the number of subarrays whose xor values is less than B.


Example Input

Input 1:

 A = [8, 3, 10, 2, 6, 7, 6, 9, 3]
 B = 3

Input 2:

 A = [9, 4, 3, 11]
 B = 7



Example Output

Output 1:

 5

Output 2:

 3



Example Explanation

Explanation 1:

 Generate all the subarrays and their corresponding xor and there are only 5 such subaraays which have xor less than 3.

Explanation 2:

 Subarrays with xor < 7 are : [9, 4, 3, 11], [4] and [3].
 So, the answer is 3.
"""
"""
Hint 1

Think of maintaining a data-structure which can store and manage all the prefix-xors ending at index i of the given array.
This can be solved using the Trie data structure.
"""
"""
Solution Approach

Use trie data structure. An efficient approach will be to calculate all of the prefix xor values i.e. a[1:i] for all i. It can be verified that the xor of a subarray a[l:r] can be written as (a[1:l-1] xor a[1:r]), where a[i, j] is the xor of all the elements with index such that, i <= index <= j.

We will store a number as binary number in trie. The left child will shows that the next bit is 0 and the right child will show the next bit is 1. If xor[i, j] represents the xor of all elements in the subarray a[i, j], then at an index i what we have is, a trie which has xor[1:1], xor[1:2]…..xor[1:i-1] already inserted. Now we somehow count how many of these (numbers in trie) are such that its xor with xor[1:i] is smaller than k. This will cover all the subarrays ending at the index i and having xor i.e. xor[j, i] <=k;
Now, to count the numbers that are below a given node, we modify the trie and each node will also store the number of leafs in that subtree and this would be modified after each insertion.

Time complexity: O(n*log(max)), where max is the maximum element in the array.
"""
class TrieNode:
    def __init__(self, b):
        self.bit = [None]*2
        self.val = b
        self.cnt = 0

    def set_next(self, i, nxt):
        self.bit[i] = nxt


def intToBinary(k):
    bin = [0]*20
    i = 0
    while(k > 0):
        bin[i] = k % 2
        k = k//2
        i = i+1
    bin.reverse()
    return bin


def insertValue(p, root):
    V = intToBinary(p)
    curr = TrieNode(1)
    curr.bit = root.bit
    curr.val = root.val
    curr.cnt = curr.cnt
    for i in range(20):
        if (curr.bit[V[i]] == None):
            curr.bit[V[i]] = TrieNode(V[i])
        curr = curr.bit[V[i]]
        curr.cnt = curr.cnt+1
    return


def query(p, k, root):
    P = intToBinary(p)
    K = intToBinary(k)
    curr = TrieNode(1)
    curr.bit = root.bit
    curr.val = root.val
    curr.cnt = curr.cnt
    ans = 0
    i = 0
    while(i < 20 and curr != None):
        if (K[i] == 0):
            if (P[i] == 1):
                curr = curr.bit[1]
            else:
                curr = curr.bit[0]
        else:
            if (P[i] == 1):
                if (curr.bit[1] != None):
                    ans = ans + curr.bit[1].cnt
                curr = curr.bit[0]
            else:
                if (curr.bit[0] != None):
                    ans = ans + curr.bit[0].cnt
                curr = curr.bit[1]
        i = i+1

    if (curr != None):
        ans = ans + curr.cnt
    return ans


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if (len(A) == 0):
            return 0

        root = TrieNode(-1)
        insertValue(0, root)
        k = 0
        res = 0
        mod = 1e9+7
        XOR = []
        XOR.append(0)
        for i in range(len(A)):
            k = k ^ A[i]
            XOR.append(k)
            s = res
            res = (res + query(k, B-1, root)) % mod
            insertValue(k, root)
            # print(root.val);
        ans = res
        return int(ans)
