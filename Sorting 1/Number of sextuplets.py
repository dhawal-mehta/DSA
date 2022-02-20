"""
Number of sextuplets


Problem Description

Given an array of integers A, find the number of sextuplets that satisfy the equation ( (a * b + c) / d ) - e = f.

where a, b, c, d, e, f belong to the given array A.

NOTE: Since the answer can be very large, return the number of ways modulo (109 + 7).



Problem Constraints

1 <= |A| <= 100

-106 <= A[i] <= 106

All elements of array A are distinct.



Input Format

The only argument given is the integer array A.


Output Format

Return the find the number of sextuplets that satisfy the equation.


Example Input

Input 1:

A = [1]

Input 2:

A = [1, -1]



Example Output

Output 1:

 1

Output 2:

 24



Example Explanation

Explanation 1:

a = b = c = d = e = f = 1 satisfy the equation.

Explanation 2:

Multiple instances satisfy the equation. Their count is 24.
"""
"""
Hint 1
Try a brute force solution.
What observations can you draw from the same??
Can you rewrite the equation in some other form??
"""
"""
Solution Approach

We can rewrite the equation in other forms.
the form is (ab) + c= d * (e + f).
You can use map to store number of occurence for each triplet.
Hence you can count the answer in O(N^3).
This is far better than the brute force solution.
for(int i=0;i<n;i++)
for(int j=0;j<n;j++)
for(int k=0;k<n;k++)
if(A[k]!=0){
mp[(A[i]+A[j])A[k]]++;}
"""
# @param A : list of integers
# @return an integer
def solve( A):
    sett = {}
    for i in A:
        for j in A:
            for k in A:
                if k != 0:
                    temp = (i + j)*k
                    if temp not in sett:
                        sett[temp] = 1
                    else:
                        sett[temp] += 1
    
    ans = 0
    for i in A:
        for j in A:
            for k in A:
                temp = i*j + k
                if temp in sett:
                    ans = ( ans + sett[temp])%(10**9 + 7)
    
    return ans