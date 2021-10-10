"""
Maximum XOR


Problem Description

Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.


Problem Constraints

1 <= length of the array <= 100000
0 <= A[i] <= 109


Input Format

The only argument given is the integer array A.


Output Format

Return an integer denoting the maximum result of A[i] XOR A[j].


Example Input

Input 1:

 A = [1, 2, 3, 4, 5]

Input 2:

 A = [5, 17, 100, 11]



Example Output

Output 1:

 7

Output 2:

 117



Example Explanation

Explanation 1:

 Maximum XOR occurs between element of indicies(0-based) 1 and 4 i.e. 2 ^ 5 = 7.

Explanation 2:

 Maximum XOR occurs between element of indicies(0-based) 1 and 2 i.e. 17 ^ 100 = 117.
 """
 """
 Hint 1
 Brute force approach is to run two loops for i and j, calcualte all possible values of A[i] ^ A[j] and find the maximum possible result.

But this approach will not pass with the given constraints. Let’s try to modify the problem a little.

Suppose you have i-1 elements and you have to find the maximum xor of ith element with i-1 elements, How will you proceed?
"""
"""
Hint 2

First think of the solution of the problem. Given i-1 elements, find the maximum xor of ith element with the previous i-1 elements.

To find the maximum XOR, It is wise to set the most significant bit to 1 first.

Get the bit representation of all the numbers, There can be two cases for the most significant bit(right most bit):
1) If the most significant bit of ith number is 1, we will take the numbers with that bit 0.
2) If the most significant bit of ith number is 0, we will take the numbers with that bit 1.

We will proceed from most significant bit to least significant bit(right to left in bit representation of a number) and keep on taking the numbers with opposite bit.

In this way, we are fixing the xor of our answer one bit at a time. Can we optimize our answer now ?

Instead of checking every element with the same prefix of bit representtion, Is there a way we can combine the numbers having same prefix bit representation?

Think of using trie data structure for this.
"""
"""
Solution Approach
As mentioned in the hints, We will find the maximum XOR of ith element with the previous i-1 elements of the array. Do this for all i 1 to N and update the maximum XOR at eact step.

First build bitwise trie of i-1 elements which means insert the bit representation(from right to left) of all i-1 elements into the trie.

For ex: Given 3 numbers with their bit representation: 6(00110) , 5(00101) and 23(10111) and we need to find the maximum xor of 2(00010) with these numbers.

Insert 6(00110), 5(00101) and (10101).
After inserting, Our trie will look like this. (using only 5 bits for example)

        -1(root)
       /   \
      0     1
     /     /
    0     0
     \     \ 
      1     1
    /   \    \
   0     1    1
    \   /      \
   (5)1 0(6)      1(23)

We want to find the maximum xor of 2(00010) with the numbers in the trie.
Start traversing in the trie from root, At every node, there can be two possibilites:

1) If the 2(00010) has 1 at that bit, move to the left means towards elements having that bit 0.
2) If the 2(00010) has 0 at that bit, move to the right means towards elements having that bit 1.

Basically move in the direction of opposite bit to set that bit in our answer to one.

Algorithm:

1) Convert numbers into binary form.
2) Add numbers into the trie one by one and compute the maximum XOR of a number to add with all previously inserted. Update maximum XOR at each step.
3) Return the maximum XOR calculated.

At every i we are checking the maximum xor with all elements from 0 to i-1. Time complexity of this step is O(log(max_element in the array)).

We are doing this for every i 1 to N. Overall time complexity is O(Nlog(max_element in the array))
"""
class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, num):
        
        curr = self.trie
        for i in range(31, -1, -1):
            bin = (num>>i) &1
            if bin not in curr:
                curr[bin] = {}
            
            curr = curr[bin]
            
            
    def query(self, num):
        curr = self.trie
        val = 0
        for i in range(31, -1, -1):
            bin = num>>i &1
            
            if 1-bin in curr:
                val += 2**i
                curr = curr[1-bin]
            else:
                if bin in curr:
                    curr = curr[bin]
                else:
                    return val
            
        return val
        
    
def solve(A):
    tr = Trie()
    
    res = 0
    
    for i in A:
        res = max(res, tr.query(i))
        tr.insert(i)
        
    return res