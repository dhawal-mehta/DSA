"""
Stacking Cubes


Problem Description

You are given A cubes that are of the same size. You are allowed to stack cubes on top of each other.

You should choose P cubes from the A cubes, such that you should stack all the remaining cubes on top of the P cubes, and each of the P cubes should have equal number of cubes on top of them.

Find and return the number of ways you can stack cubes on top of each other in the given manner.

NOTE: Every cube has to be stacked, you cannot have unstacked cubes. No stack can consist of a total of just one cube.



Problem Constraints

2 <= A <= 105


Input Format

First and only argument is an integer A denoting number of cubes.


Output Format

Return an integer denoting the number of ways you can stack cubes on top if each other in the above given manner.


Example Input

Input 1:

 A = 2

Input 2:

 A = 6



Example Output

Output 1:

 1

Output 2:

 3



Example Explanation

Explanation 1:

 Only one cube is stacked on another cube.

Explanation 2:

 You can have 5 cubes stacked on one cube, or 2 cubes stacked on one cube with a total of two stacks, 
 or 1 cube stacked on one cube with a total of 3 stacks."""
"""
Hint 1

If you have i stacks, you will need the remaining N-i cubes to uniformly be distributed on the i stacks, basically (N-i)%i==0
"""
"""
Solution Approach

We basically need to find out the number of ways in which we can uniformly distribute N-i cubes over i cubes (1 <= i <= N/2). This is possible only when N-i is perfectly divisible by i.

Once i > N/2, the answer can never exist.

We have N cubes:
    Distribute N-1 cubes on 1 cube, if (N-1)%1 == 0 (obviously)
    Distribute N-2 cubes on 2 cubes, if (N-2)%2 == 0 
    Distribute N-3 cubes on 3 cubes, if (N-3)%3 == 0 
    This goes on until... 
    Distribute N-N/2 cubes on N/2 cubes, if (N-N/2)%(N/2) == 0

Increment the answer by 1 for each condition that satisfies.
"""
# @param A : integer
# @return an integer



def solve(self, A):
    num = [1]*(10**5 + 5)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
    # primes = []
    num[0] = -1
    num[1] = -1
    primePtr = 0
    ans = 1
    while A != 1:
        count = 1   # count is one because we will be multipling by (count+1)
        
        if primePtr < len(primes) and A%primes[primePtr] == 0:
            # print(primes[primePtr])
            
            while A%primes[primePtr] == 0:
                count += 1
                A = A/primes[primePtr]
                
            ans *= count
        elif  primePtr >= len(primes):
            return ans*(count + 1) -1 
            # break
        else:
            primePtr+=1
    # -1 is to remove the case of no stacking ie tower of 1 cube
    return ans-1