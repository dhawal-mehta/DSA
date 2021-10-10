"""Hire candidates


Problem Description

A company wants to hire maximum number of students from a college. The company cannot spend more than A amount to hire students.

There are N students numbered 1 to N and the base cost to hire students is given by an integer array B of size N.

The final cost of students depends on the number of students the company hire.
If a company hires X students then the final cost to hire the ith student will be B[i] + (iX) (where i is the number of that student).

Find the maximum value of X and the minimum cost to hire X people.

NOTE: Cost to hire students X should be less than equal to A.



Problem Constraints

1 <= N <= 100000

1 <= A, B[i] <= 109



Input Format

First argument is an integer A.
Second argument is an integer array B.


Output Format

Return an integer array of size 2, first element denoting maximum value of X and second element denoting the minimum cost to hire X students.


Example Input

 A = 20
 B = [9, 4, 2, 3,  2]



Example Output

 [2, 16]



Example Explanation*

 We can select maximum of 2 students then the final cost of each student will be [11, 8, 8, 11, 12].
 For student 1: 9 + 1 * 2 = 11
 For student 2: 4 + 2 * 2 = 8
 For student 3: 2 + 3 * 2 = 8
 For student 4: 3 + 4 * 2 = 11
 For student 5: 2 + 5 * 2 = 12
 So, the minimum cost of selecting two students will be 16.
 
 """
"""
Hint 1

For all X (1<=X<=N) check the minimum cost is we hire X candidates. If the cost comes out to be less than A then we can hire X students.

Such that find the maximum X.

The time complexity for this will be O(N2).

Can you optimize it. Think of using Binary Search.
"""
"""
Solution Approach

We can solve this problem by using binary search. The value of X range between 0 to N.

If the company hires X students and the minimum cost for X candidates is less than equal to A then we don’t need to check for values less than X.
If the minimum cost to hire X students greater than A so no need to check for values greater than X.

Like that we can use a binary search in O(Log(N)) and to find the minimum cost it take O(N log(N)).

Time Complexity : O(N log2N).
"""
def solve(self, A, B):
    def isPossible(N, A, tempB):
        for i in range( len(tempB) ):
            tempB[i] = tempB[i] + (i+1)*N
        
        tempB = sorted(tempB)
        sum_ = sum(tempB[:N])

        return [True, sum_]  if sum_ <= A else [False, sum_]

    

    L = 0
    minL = 0
    minsm=0
    R = len(B)

    while L<R:
        mid = (L+R)//2
        check, sum_ = isPossible(mid, A, B[::])

        if check:
            minL = mid
            minsm = sum_
            L = mid+1
        else:
            R = mid
    
    return [minL, minsm]

