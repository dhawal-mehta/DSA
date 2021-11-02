"""
Gas Station


Given two integer arrays A and B of size N. There are N gas stations along a circular route, where the amount of gas at station i is A[i].

You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.

You can only travel in one direction. i to i+1, i+2, … n-1, 0, 1, 2.. Completing the circuit means starting at i and ending up at i again.


Input Format

The first argument given is the integer array A.
The second argument given is the integer array B.

Output Format

Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.

For Example

Input 1:
    A =  [1, 2]
    B =  [2, 1]
Output 1:
    1
    Explanation 1:
        If you start from index 0, you can fill in A[0] = 1 amount of gas. Now your tank has 1 unit of gas. But you need B[0] = 2 gas to travel to station 1. 
        If you start from index 1, you can fill in A[1] = 2 amount of gas. Now your tank has 2 units of gas. You need B[1] = 1 gas to get to station 0. So, you travel to station 0 and still have 1 unit of gas left over. You fill in A[0] = 1 unit of additional gas, making your current gas = 2. It costs you B[0] = 2 to get to station 1, which you do and complete the circuit. 
"""
"""
Hint 1
Try to find the relation between sum of gas and sum of cost for solution to exist.

When will you shift your starting point from 0?
Do you really need to cover every starting point? How can you use answer of above question to optimize this part?
"""
"""
Solution Approach

The bruteforce solution should be obvious. Start from every i, and check to see if every point is reachable with the gas available. Return the first i for which you can complete the trip without the gas reaching a negative number.
This approach would however be quadratic.

Lets look at how we can improve.
1) If sum of gas is more than sum of cost, does it imply that there always is a solution ?
2) Lets say you start at i, and hit first negative of sum(gas) - sum(cost) at j. We know TotalSum(gas) - TotalSum(cost) > 0. What happens if you start at j + 1 instead ? Does it cover the validity clause for i to j already ?
"""

def canCompleteCircuit(self, A, B):
    if len(A) == 1:
        return 0
    
    gas = A
    cost = B
    
    end = -1
    curr = 0  #non processed next
    count = 0 # num of elements processed
    starts = 0 # how many starts have been processed
    
    gas_curr = 0
    
    while True:
        if starts >= len(A) and curr == 0 and count != len(A):
            return -1
            
        if curr == end and count == len(A):
            return curr
        
        elif gas_curr + A[curr] - B[curr] >= 0:
            gas_curr += A[curr] - B[curr]
            
            if end == -1:
                end = curr
                
            count += 1
            # starts += 1
            curr = ( curr + 1 )%len(A)
        else:
            if count >= 1:
                gas_curr -=  A[end] - B[end]
                count -= 1
                starts += 1
                end = (end + 1)%len(A) if count != 0 else -1
            elif  count == 0:
                end = -1
                starts += 1
                curr = ( curr + 1 )%len(A)