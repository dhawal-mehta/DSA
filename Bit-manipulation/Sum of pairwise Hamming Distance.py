"""
Sum of pairwise Hamming Distance

Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

For example,

HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.

Example

Let f(x, y) be the hamming distance defined above.

A=[2, 4, 6]

We return,
f(2, 2) + f(2, 4) + f(2, 6) + 
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) = 

0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8

"""
"""
Hint 1
Suppose the given array contains only binary numbers, i.e A[i] belongs to [0, 1].

You only need to find the number of pairs having different bits.

Try to combine this approach if we have array of integers instead of binary numbers containing multiple bits.
"""
"""
Solution Approach

Suppose the given array contains only binary numbers, i.e A[i] belongs to [0, 1].

Let X be the number of elements equal to 0, and Y be the number of elements equals to 1.

Then, sum of hamming distance of all pair of elements equals 2XY, as every pair containing one element from X and one element from Y contribute 1 to the sum.

As A[i] belongs to [0, 231 - 1] and we are counting number of different bits in each pair, we can consider all the 31 bit positions independent.

For example:
A = [2, 4, 6] = [0102, 1002, 1102]</p>

At bit position 0 (LSB): x = 3, y = 0
At bit position 1: x = 1, y = 2
At bit position 2(MSB): x = 1, y = 2

Total sum = number of pairs having different bit at each bit-position = (2 * 3 * 0) + (2 * 1 * 2) + (2 * 1 * 2) = 8

Time complexity: O(N)
Space complexity: O(1)

"""


# @param A : tuple of integers
# @return an integer
def hammingDistance(A):
    
    count = 0
    for i in range(31, -1, -1):
        ones = 0
        zeros = 0
        for j in range(len(A)):
            num = (A[j]>>i)&1
            if num == 1:
                ones += 1
            else:
                zeros += 1
        
        count += 2*ones*zeros
                
    
    return count