"""
Task Scheduler

Given a string A representing tasks CPU need to do it. A consists of uppercase English letters where different letters represent different tasks. Tasks could be done without the original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval B that means between two same tasks, there must be at least B intervals that CPU is doing different tasks or just be idle.

Find the least number of intervals the CPU will take to finish all the given tasks.


Input Format

The first argument given is string A.
The second argument given is an integer B.

Output Format

Return the least number of intervals the CPU will take to finish all the given tasks.

Constraints

1 <= |A| <= 10000
0 <= B <= 100 

For Example

Input 1:
    A = "AAABBB"
    B = 2
Output 1:
    8
    Explanation 1:
        CPU can finish the tasks in one of the following ways:
            A -> B -> idle -> A -> B -> idle -> A -> B.
            B -> A -> idle -> B -> A -> idle -> B -> A.

Input 2:
    A = "DBAD"
    B = 5
Output 2:
    7
    Explanation 2:
        D -> B -> A -> idle -> idle -> idle -> D
"""
# @param A : string
# @param B : integer
# @return an integer
def solve(self, A, B):
    
    if B==0:
        return len(A)

    alphaSet = {}

    for i in A:
        try:
            alphaSet[i] += 1
        except:
            alphaSet[i] = 1
    ans = 0
    t = 0
    B += 1

    removedAlpha = 0
    while alphaSet:
        tempT = 0
        for i in alphaSet.keys():
            if alphaSet[i] > 0:
                alphaSet[i] -= 1

                if alphaSet[i] == 0:
                    removedAlpha +=1
            
                tempT += 1

            if tempT == B:
                break
        # print(tempT)
        if tempT < B:
            if removedAlpha < len(alphaSet):
                ans += B
            else:
                ans += tempT
                return ans
        else:
            ans += tempT