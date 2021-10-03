""" 
Number of Digit 


Problem Description

Given an integer A, find and return the total number of digit 1 appearing in all non-negative integers less than or equal to A.


Problem Constraints

0 <= A <= 109


Input Format

The only argument given is the integer A.


Output Format

Return the total number of digit 1 appearing in all non-negative integers less than or equal to A.


Example Input

Input 1:

 A = 10

Input 2:

 A = 11



Example Output

Output 1:

 2

Output 2:

 4



Example Explanation

Explanation 1:

Digit 1 appears in 1 and 10 only and appears one time in each. So the answer is 2.

Explanation 2:

Digit 1 appears in 1(1 time) , 10(1 time) and 11(2 times) only. So the answer is 4.
"""
"""
Hint 1
Simple solution is to traverse from 1 to A and count the number of 1 appearing in each digit.
"""
"""
Solution Approach
Brute force solution of traversing all numbers from 1 to A and counting the number of 1s in each number will not pass with the given constraints.

Try to approach the problem in a different way.

Let’s just figure out the number of 1s at one’s place, a number of 1s in second place and so on. We will add all these occurrences of 1s.

At one’s place:
up to 10, there is 1 one.
up to 20, there are 2 one’s.
.
.
up to 131, there are 14 one’s
up to 13x(x>1), there are 14 one’s.

Number of 1’s at one’s position = (n/10) + (n%10!=0)

Try to find the formula for ten’s place, hundred’s place and so on.

Solution can be summarised into 4 steps:
1) Initialize ans = 0
2) Iterate over i from 1 to n incrementing by 10 times in each iteration.
3) Add (n / (i * 10 ) ) * i to ans after each (i * 10) interval.
4) Add min( max((n mod (i * 10) – i + 1, 0), i) to ans.
"""
"""Accepted Solution"""
def solve(A):
    res = 0
    num = A 
    base = 1
    while num>0:
        rem = num%10
        
        for i in range(rem):
            if i == 1:
                res += 10**(base-1)

            res += (base-1)*(10**(base-2))
        
        
        if rem == 1:
            res += A%(10**(base - 1)) + 1
        
        num = num//10
        base += 1
    return int(res)