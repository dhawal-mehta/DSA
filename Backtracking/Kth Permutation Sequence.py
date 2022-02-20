"""
Kth Permutation Sequence


The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, We get the following sequence (ie, for n = 3 ) :

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.

For example, given n = 3, k = 4, ans = "231"

    Good questions to ask the interviewer :

        What if n is greater than 10. How should multiple digit numbers be represented in string?

        In this case, just concatenate the number to the answer. so if n = 11, k = 1, ans = "1234567891011"

        Whats the maximum value of n and k?

        In this case, k will be a positive integer thats less than INT_MAX. n is reasonable enough to make sure the answer does not bloat up a lot.

"""
"""
Hint 1

Note: Generating all permutation wont help here.

What you can do is try out elements which can you keep at any position. If the permutation resulting from keeping this element does not becomes >= k you keep incrementing the element to be put.

Can you see now how recursion and maths can help us here now?
"""
"""
Solution Approach

This involves a little bit of maths and recursion for simplicity.

Number of permutation possible using n distinct numbers = n!

Lets first make k 0 based.
Let us first look at what our first number should be.
Number of sequences possible with 1 in first position : (n-1)!
Number of sequences possible with 2 in first position : (n-1)!
Number of sequences possible with 3 in first position : (n-1)!

Hence, the number at our first position should be k / (n-1)! + 1 th integer.

Can we reduce the k and modify the set we pick our numbers from ( initially 1 2 3 … n ) to call the function for second position onwards ?
"""
"""
Solution Approach

This involves a little bit of maths and recursion for simplicity.

Number of permutation possible using n distinct numbers = n!

Lets first make k 0 based.
Let us first look at what our first number should be.
Number of sequences possible with 1 in first position : (n-1)!
Number of sequences possible with 2 in first position : (n-1)!
Number of sequences possible with 3 in first position : (n-1)!

Hence, the number at our first position should be k / (n-1)! + 1 th integer.

Can we reduce the k and modify the set we pick our numbers from ( initially 1 2 3 … n ) to call the function for second position onwards ?
Solution Approach

This involves a little bit of maths and recursion for simplicity.

Number of permutation possible using n distinct numbers = n!

Lets first make k 0 based.
Let us first look at what our first number should be.
Number of sequences possible with 1 in first position : (n-1)!
Number of sequences possible with 2 in first position : (n-1)!
Number of sequences possible with 3 in first position : (n-1)!

Hence, the number at our first position should be k / (n-1)! + 1 th integer.

Can we reduce the k and modify the set we pick our numbers from ( initially 1 2 3 … n ) to call the function for second position onwards ?
"""
import math
class Solution:
    def getP(self,strs,st,n,k,nf):
        if k==0 or st>n-1:
            return
        else:
            l=k/math.factorial(n-st-1)
            p=strs.pop(st+l)
            strs.insert(st,p)
            k=k%math.factorial(n-st-1)
            self.getP(strs,st+1,n,k,nf)
        return
     
    # @return a string
    def getPermutation(self, n, k):
        strs = [str(x) for x in range(1,n+1)]
        nf=[1,1,2,6,24,120,720,5040,40320,362880, 3628800, 39916800]
        st=0
        k=k-1
        self.getP(strs,st,n,k,nf)
        return "".join(x for x in strs)