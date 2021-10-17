"""Special Integer

Problem Description

Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B.


Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 10^9

1 <= B <= 10^9


Input Format

The first argument given is the integer array A.

The second argument given is integer B.



Output Format

Return the maximum value of K (sub array length).


Example Input

Input 1:

A = [1, 2, 3, 4, 5]
B = 10

Input 2:

A = [5, 17, 100, 11]
B = 130



Example Output

Output 1:

 2

Output 2:

 3



Example Explanation

Explanation 1:

Constraints are satisfied for maximal value of 2.

Explanation 2:

Constraints are satisfied for maximal value of 3.
""""""
Hint 1

you need to find the maximal K.
Can you think of a way to this by binary search??
"""
"""
Solution Approach

you need to find the maximal K.
Think of a way to this by binary search.
You can use binary seacrh to find if a certain K is allowed or not.
if it is, you try finding a bigger answer
if not, try finding a smaller answer.
int l = 1, r = a.length;
while(l <= r) {
    int m = (l + r) » 1;
    if(check(a, b, m)) l = m + 1;
    else r = m - 1;
}
return l-1;
"""
# @param A : list of integers
# @param B : integer
# @return an integer
def solve(self, A, B):
    
    if len(A)== 0 or max(A) > B :
        # print("tesfjkl")
        return 0
    
    left = 1
    right = len(A)
    
    while left <= right:
        
        mid = (right + left)//2
        res = True
        currSum = 0
        
        for i in range(len(A)):
            if i < mid:
                currSum += A[i]
            else:
                currSum -= A[i - mid]
                currSum += A[i]
                
            if currSum > B:
                res = False
                break

        if res == False:
            right = mid-1
        else:
            left = mid+1        

    if res == True:
        return mid
    else:
        return mid-1
