"""
Gray Code


Problem Description

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

A gray code sequence must begin with 0.



Problem Constraints

1 <= A <= 16


Input Format

First argument is an integer A.


Output Format

Return an array of integers representing the gray code sequence.


Example Input

Input 1:

A = 2

Input 1:

A = 1



Example Output

output 1:

[0, 1, 3, 2]

output 2:

[0, 1]



Example Explanation

Explanation 1:

for A = 2 the gray code sequence is:
    00 - 0
    01 - 1
    11 - 3
    10 - 2
So, return [0,1,3,2].

Explanation 1:

for A = 1 the gray code sequence is:
    00 - 0
    01 - 1
So, return [0, 1].
"""
"""
Hint 1

The bruteforce method would be to start with 0, change any of the bits, keeping track of the numbers already constructed. When you run into a number where there is no way forward possible, you backtrack, and try to change some other bit instead.
This might however be inefficient.

You need to come up with something smart this time.

You can notice that if a sequence is gray code, then its reverse is also a gray code. How can you use this to construct the solution?
"""
"""
Solution Approach

Note the following :

Let G(n) represent a gray code of n bits.
Note that reverse of G(n) is also a valid sequence.
Let R(n) denote the reverse of G(n).

Note that we can construct
G(n+1) as the following :
0G(n)
1R(n)

Where 0G(n) means all elements of G(n) prefixed with 0 bit and 1R(n) means all elements of R(n) prefixed with 1.
Note that last element of G(n) and first element of R(n) is same. So the above sequence is valid.

Example G(2) to G(3) :
0 00
0 01
0 11
0 10
1 10
1 11
1 01
1 00
"""

"""
public class Solution {
    public ArrayList < Integer > grayCode(int A) {
        int n = A;
        ArrayList < Integer > result = new ArrayList < > ();
        result.add(0);
        for (int i = 0; i < n; i++) {
            int curSize = result.size();
            // push back all element in result in reverse order
            for (int j = curSize - 1; j >= 0; j--) {
                result.add(result.get(j) + (1 << i));
            }
        }
        return result;
    }
}
"""
# do not understand this approach properly

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        ans = []
        for i in xrange(2 ** A):
            ans.append((i>>1) ^ i)
        return ans